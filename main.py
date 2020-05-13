from dsc.cmdline import parse_cmdline
from dsc.issue import GithubIssue
from dsc.params import SendEmailParams
from dsc.invoice import InvoiceHTMLParser
from dsc.email import Email, EmailTemplate


def main():
    """Execute other functions in script.

    Executes:
        parse_cmdline() -- command-line interface
    """
    parser = InvoiceHTMLParser()
    args = parse_cmdline()
    issue = GithubIssue(
        token=args.token,
        repository=args.repository,
        organization=args.organization
    )
    parser.feed(issue.html(args.issueid))

    template = EmailTemplate()

    with open("template/update_template.html", 'r') as f:
        update = f.read()

    template.make_content(update)

    email = Email(endpoint=args.endpoint, api_key=args.apikey)
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


if __name__ == "__main__":
    main()
