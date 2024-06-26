import os
import json

indexedTypes = None


def define_env(env):
    @env.macro
    def type_url(type):
        global indexedTypes
        if indexedTypes is None:
            # open types.json and store parse the json
            with open(os.path.join(os.path.dirname(__file__), 'types.json')) as f:
                data = json.load(f)
                # It's a list of objects. We'll store the dictionary with the 'name' as the key and 'id' as the value.
                # we also put the name in lowercase to make it not case-insensitive
                indexedTypes = {t['name'].lower(): t['id'] for t in data}
        # return the url
        if type.lower() not in indexedTypes:
            return f'https://docs.skunity.com/syntax/search/type:Types+{type}'

        return f'https://docs.skunity.com/syntax/search/id:{indexedTypes[type.lower()]}'

    def required_version(version):
        return f"""
        <span class="mdx-badge"><span class="mdx-badge__icon"><a href="" title="Required DiSky Version XXX"><span
        class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                                        <path
                                                d="m21.41 11.58-9-9A2 2 0 0 0 11 2H4a2 2 0 0 0-2 2v7a2 2 0 0 0 .59 1.42l9 9A2 2 0 0 0 13 22a2 2 0 0 0 1.41-.59l7-7A2 2 0 0 0 22 13a2 2 0 0 0-.59-1.42M13 20l-9-9V4h7l9 9M6.5 5A1.5 1.5 0 1 1 5 6.5 1.5 1.5 0 0 1 6.5 5Z">
                                        </path>
                                </svg></span></a></span><span class="mdx-badge__text"><a
        href="https://modrinth.com/plugin/disky/">Requires DiSky v{version}</a></span></span>
        """

    env.macro['required_version'] = required_version

    def return_type(type):
        return f"""
            <span class="mdx-badge"><span class="mdx-badge__icon"><a href="" title="Return Type"><span
                    class="twemoji"><svg fill="#1C2033" width="52" height="52" version="1.1" id="lni_lni-arrow-left" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 64 64" style="enable-background:new 0 0 64 64;" xml:space="preserve"> <path d="M56,29.8H13.3l17-17.3c0.9-0.9,0.9-2.3,0-3.2c-0.9-0.9-2.3-0.9-3.2,0l-20.7,21c-0.9,0.9-0.9,2.3,0,3.2l20.7,21 c0.4,0.4,1,0.7,1.6,0.7c0.6,0,1.1-0.2,1.6-0.6c0.9-0.9,0.9-2.3,0-3.2L13.4,34.3H56c1.2,0,2.2-1,2.2-2.2C58.2,30.8,57.2,29.8,56,29.8 z"/> </svg>
            </span></a></span><span class="mdx-badge__text">Returns {type}</span></span>"""

    env.macro['return_type'] = return_type
