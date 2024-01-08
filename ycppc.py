import re

ycppc_indication_re = re.compile(r"<!-- YCPPC: (\S+) -->")

tilde_normalized_head_tags = """<!-- YCPPC generated tags for tilde-normalized-head-tags begin -->
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<style>
html { color-scheme: light dark; }
body {
    margin: 0 auto;
    font-family: Tahoma, Verdana, Arial, sans-serif;
    max-width: 35em;
    padding: 1em;
    background-color: #fafafa;
}
@media (prefers-color-scheme: dark) {
    body {
        background-color: black;
    }
}
</style>
<!-- YCPPC generated tags for tilde-normalized-head-tags end -->"""

def apply(text):
    def replacer(matchobj):
        kind = matchobj.group(1)
        match kind:
            case "tilde-normalized-head-tags":
                return tilde_normalized_head_tags
            case unimpl:
                raise ValueError(f"Invalid ycppc kind: {unimpl}")
        
    res = ycppc_indication_re.sub(replacer, text)
    return res