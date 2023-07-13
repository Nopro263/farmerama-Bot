import urllib.parse
import urllib.request
import html.parser


def _mimic_user(url: str) -> urllib.request.Request:
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0")
    req.add_header("Accept",
                   "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")
    req.add_header("Accept-Encoding", "utf-8")
    return req

def create_account(username: str, password: str, email: str, newsletter: bool = False):
    initial_req = _mimic_user("https://farmerama.com")
    initial_data = urllib.request.urlopen(initial_req).read().decode("utf-8")

    fex = formextractor()
    fex.feed(initial_data)

    register_url = fex.action
    register_req = _mimic_user(register_url)
    register_data = {
        "username": username,
        "password": password,
        "email": email,
        "termsAndConditions": "1",
        "newsletter": str(int(newsletter))
    }
    register_data = urllib.parse.urlencode(register_data).encode("utf-8")

    urllib.request.urlopen(register_req, register_data).read().decode("utf-8")


def _argsToDict(_in: list) -> dict:
    res = {}
    for attr in _in:
        res[attr[0]] = attr[1]
    return res


class formextractor(html.parser.HTMLParser):

    def __init__(self, convert_charrefs=True):
        self.action = ""
        super().__init__(convert_charrefs=convert_charrefs)
    def handle_starttag(self, tag, _attrs):
        attrs = _argsToDict(_attrs)
        if tag == "form":
            if 'name' in attrs and "signup" in attrs['name']:
                self.action = attrs['action']
