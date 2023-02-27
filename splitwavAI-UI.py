import flet as ft
from handleWavTest import splitwavAI


def main(page: ft.Page):
    def file_pick_result(e: ft.FilePickerResultEvent):
        if e.files:
            fpath = e.files[0].path
            print(e.files)
            text_path.value = fpath
            btn_handle.disabled = False
        else:
            text_path.value = "未打开任何文件！"
        page.update()

    def file_handle(e):
        if file_picker.result.files:
            print("chenxxx想知道的-----")
            print(file_picker.result.files[0].path)
            print("chenxxx想知道的-----")
            splitwavAI(file_picker.result.files[0].path)
            page.add(ft.Text("处理结束！拆分后的特效轨wav文件生成在同目录下！", bgcolor="green"))
            page.update()
        else:
            page.add(ft.Text("请先选择wav文件", bgcolor="red"))
            page.update()

    page.title = "splitwavAI UI 1.0"
    page.scroll = ft.ScrollMode.AUTO
    file_picker = ft.FilePicker(on_result=file_pick_result)
    btn_open = ft.ElevatedButton("选择wav文件", on_click=lambda _: file_picker.pick_files(allowed_extensions=["wav"]))
    text_path = ft.Text("文件路径", bgcolor="yellow")
    btn_handle = ft.ElevatedButton("生成特效轨文件", disabled=True, on_click=file_handle)

    page.overlay.append(file_picker)
    page.add(ft.Row([btn_open, text_path]))
    page.add(ft.Row([btn_handle]))
    page.update()


ft.app(target=main)
# ft.app(target=main, view=ft.WEB_BROWSER)
