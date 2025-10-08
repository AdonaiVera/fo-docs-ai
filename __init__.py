import fiftyone.operators as foo
import fiftyone.operators.types as types

DOCS_URL = "https://docs.voxel51.com"

class DocsAIPanel(foo.Panel):
    @property
    def config(self):
        return foo.PanelConfig(
            name="docs_ai_panel",
            label="Docs AI",
            surfaces=["panel"],
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

class OpenDocsAIPanel(foo.Operator):
    @property
    def config(self):
        return foo.OperatorConfig(
            name="open_docs_ai_panel",
            label="Open Docs AI Panel",
            unlisted=True,
        )

    def resolve_placement(self, ctx):
        return types.Placement(
            types.Places.SAMPLES_GRID_ACTIONS,
            types.Button(
                label="Open Docs AI",
                icon="/assets/dark.svg",
                prompt=False,
            ),
        )

    def execute(self, ctx):
        ctx.trigger(
            "open_panel",
            params=dict(name="docs_ai_panel", isActive=True, layout="horizontal"),
        )


def register(p):
    p.register(DocsAIPanel)
    p.register(OpenDocsAIPanel)
