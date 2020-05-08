"""Generate html body of update message"""


def send_body():
    return """
<body>
    <div class="container">
        <div class="row dsc-header blue darken-4 white-text">
            <div class="col s12 m9">
                <h4>
                    <strong>Dicty Stock Center</strong>
                </h4>
            </div>
        </div>
        <div class="card-panel">
            <div>
                <h5 class="blue-text text-darken-4">
                    <strong>Order # $issue_id Update</strong>
                </h5>
            </div>
            <div class="divider"></div>
            <div class="row shipping-row grey lighten-5"></div>
            <p>Dear $user,</p>
            <p><strong>Your order status: $label </strong></p>
            <p>Please let us know if you have any questions.</p>
            <p>Best regards,</p>
            <p>The DSC Team</p>
            <a class="blue-text text-darken-1" href="dictystocks@northwestern.edu">dictystocks@northwestern.edu
            </a>
        </div>
    </div>
    </div>
</body>"""
