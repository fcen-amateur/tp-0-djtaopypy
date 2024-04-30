import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(
            gapminder[gapminder["country"].isin(["Argentina", "Bolivia", "Brazil", "Chile", "Paraguay"])],
            x="year",
            y="gdpPercap",
            color="country",
        )
        .add(so.Line())
        .label(
            title="PBI per Capita de Argentina y países limítrofes",
            x="Año",
            y="PBI per Capita (USD)",
            color="País",
        )
    )
    return dict(
        descripcion="Evolución del PBI per Cápita de Argentina y sus países limítrofes a través de los años",
        autor="Fidel Urrutia",
        figura=figura,
    )
