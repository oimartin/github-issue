from dsc.cmdline import parse_cmdline
from dsc.issue import GithubIssue
from dsc.params import SendEmailParams
from dsc.invoice import InvoiceHTMLParser
from dsc.email import Email, EmailTemplate
import os
import sys

TEMPLATE_FOLDER = os.path.join(os.path.dirname(__file__), 'template')


def main():
    """Execute modules to send order update email to DSC users."""
    parser = InvoiceHTMLParser()
    args = parse_cmdline()
    issue = GithubIssue(
        token=args.token,
        repository=args.repository,
        organization=args.organization
    )
    try:
        parser.feed(issue.html(args.issueid))
    except Exception:
        issue.comment_status(args.issueid,
                             'Could not send update email to user.')
        issue.remove_label(args.issueid, args.label)
        sys.exit('Could not send email to user.')

    file = os.path.join(TEMPLATE_FOLDER, 'update_template.html')

    try:
        os.path.exists(file) is True
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        sys.exit("Email update template was not found.")
    else:
        try:
            with open(file, 'r') as f:
                content = f.read()
        except RuntimeError as error:
            print(error)
            sys.exit("Could not read order update template file.")

    template = EmailTemplate(message=content)

    email = Email(endpoint=args.endpoint, api_key=args.apikey)

    try:
        email.send(SendEmailParams(
            sender=args.sender,
            to=parser.get_shipping_email(),
            subject=template.generate_subject(
                issue_id=parser.get_order_id(),
                label=args.label
            ),
            content=template.generate_content(
                user=parser.get_user_name(),
                label=args.label,
                issue_id=parser.get_order_id()
            )
        ))
        issue.comment_status(args.issueid,
                             'Successfully sent update email to user.')
    except Exception:
        issue.comment_status(args.issueid,
                             'Could not send update email to user.')
        issue.remove_label(args.issueid, args.label)
        sys.exit('Could not send email to user.')


if __name__ == "__main__":
    main()
