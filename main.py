from kivy.app import App
from kivy.lang import Builder

from database import *
from analyzer import *
from predictor import *

KV = Builder.load_file("ui.kv")


class PredictorApp(App):

    def build(self):

        init_db()
        self.update_total()

        return KV


    def update_total(self):

        numbers = get_numbers()

        try:
            self.root.ids.total_data.text = f"Total Data : {len(numbers)}"
        except:
            pass


    def save_number(self):

        num = self.root.ids.input_num.text

        if len(num) != 4:

            self.root.ids.result.text = "Input harus 4 digit"
            return

        insert_number(num)

        self.root.ids.result.text = "Data tersimpan"

        self.root.ids.input_num.text = ""

        self.update_total()


    def run_prediction(self):

        numbers = get_numbers()

        if len(numbers) < 10:

            self.root.ids.result.text = "Minimal 10 data"
            return

        pos = position_frequency(numbers)

        preds = generate_prediction(pos)

        self.root.ids.result.text = "\n".join(preds)


    def show_history(self):

        numbers = get_numbers()

        if not numbers:

            self.root.ids.result.text = "Belum ada data"
            return

        history = "\n".join(numbers[-50:])

        self.root.ids.result.text = history



PredictorApp().run()