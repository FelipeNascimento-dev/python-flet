import flet as ft
from flet import colors


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK

    def change_main_image(e):
        ...

    product_images = ft.Container(
        content=ft.Column(
            controls=[
                ft.Image(
                    src='https://http2.mlstatic.com/D_NQ_NP_995457-MLU70206250479_062023-O.webp',
                ),

                ft.Row(
                    controls=[
                        ft.Container(
                            image_src='https://http2.mlstatic.com/D_NQ_NP_995457-MLU70206250479_062023-O.webp',
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image
                        ),

                        ft.Container(
                            image_src='https://http2.mlstatic.com/D_NQ_NP_724328-MLU71482869531_092023-O.webp',
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image
                        ),

                        ft.Container(
                            image_src='https://http2.mlstatic.com/D_NQ_NP_753888-MLU71571167899_092023-O.webp',
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image
                        )
                    ]
                )
            ]
        )
    )

    product_details = ft.Container()

    layout = ft.Container(
        width=900,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                product_images,
                product_details
            ]
        )
    )

    page.add(layout)   

if __name__ == '__main__':
    ft.app(target=main)