import fiftyone.operators as foo
import fiftyone.operators.types as types

DOCS_URL = "https://docs.voxel51.com"  

class DocsAIPanel(foo.Panel):
    @property
    def config(self):
        return foo.PanelConfig(
            name="docs_ai_panel",
            label="Docs AI",
            icon="/assets/atom.svg",
            dark_icon="/assets/atom.svg",
            light_icon="/assets/atom.svg",
            surfaces=["panel"]
        )

    def render(self, ctx):
        panel = types.Object()

        panel.define_property(
            "docs_ai_iframe",
            types.String(),
            view=types.HeaderView(
                label="Docs AI",
                componentsProps={
                    "label": {
                        "component": "iframe",
                        "src": DOCS_URL,
                        "border": "none",
                        "style": {
                            "width": "100%",
                            "height": "100%",
                            "position": "absolute",
                            "top": "20px",
                            "left": "0",
                            "z-index": "1"
                        }
                    }
                },
            ),
        )

        return types.Property(panel, view=types.View(
            sizing_mode="stretch_both",
            width="100%",
            height="100%"
        ))


def register(p):
    p.register(DocsAIPanel)
