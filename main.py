from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDRectangleFlatIconButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from db_connect import cur
from kivy.uix.image import Image
import os
from kivy.uix.screenmanager import Screen, ScreenManager, WipeTransition
from screen_mg import screen_manager as screen_manager
import json
from db_connect import conn
from kivy.uix.button import Button


class LoginScreen(Screen):
    username_inputs = ()
    password_inputs = ()
    username_list = ()
    password_list = ()
    username_verified = ()
    password_verified = ()

    def get_data(self):
        print('[LOGIN]The data of username text field is: ', self.ids.user.text)
        self.username_inputs = self.ids.user.text
        print(self.username_inputs)
        print('[LOGIN]The data of password text field is: ', self.ids.pw.text)
        self.password_inputs = self.ids.pw.text
        print(self.password_inputs)

        cur.execute('SELECT USERNAME from VoyagerKV_reg')
        self.username_list = [item[0] for item in cur.fetchall()]
        print('DB USERNAME LIST: ', self.username_list)
        self.username_verified = ()
        if self.username_inputs in self.username_list:
            print(f'The username > {self.username_inputs} < is in the database.')
            self.username_verified = self.username_inputs
            print(f'The username > {self.username_verified} < is verified.')
            try:
                username_test = self.username_verified
                cur.execute("SELECT PASSWORD FROM VoyagerKV_reg WHERE USERNAME = %s", [username_test])
                self.password_list = [item[0] for item in cur.fetchall()]
                print('DB PASSWORD LIST: ', self.password_list)
                pass
            except (Exception, ):
                print(f"::::: > {self.password_inputs_inputs} < This password is not in the database.")
            else:
                self.password_verified = ()
                if self.password_inputs in self.password_list:
                    self.password_verified = self.password_inputs
                    print(f'The password > {self.password_verified} < match the username > {self.username_verified} <.')
                    print(f'The password > {self.password_verified} is verified. <')
                    pass
        else:
            print(f"::::: > {self.username_inputs} < This username is not in the database.")
            pass


class RegScreen(Screen):
    username_list = ()
    email_list = ()

    def get_data_reg(self):
        print('[REG]The data of username input text field is: ', self.ids.user_reg.text)
        print('[REG]The data of email input text field is: ', self.ids.email_reg.text)
        print('[REG]The data of password input text field is: ', self.ids.pw_reg.text)
        print('[REG]The data of password confirmation input text field is: ', self.ids.pw_reg_2.text)

        cur.execute('SELECT USERNAME from VoyagerKV_reg')
        self.username_list = [item[0] for item in cur.fetchall()]
        cur.execute('SELECT EMAIL_ADDRESS from VoyagerKV_reg')
        self.email_list = [item[0] for item in cur.fetchall()]

        if self.ids.user_reg.text in self.username_list:
            print('This username is already taken.')
        elif self.ids.email_reg.text in self.email_list:
            print('This email address is already taken.')
            pass
        else:
            print('Successful registration.')
            self.import_data(self.ids.user_reg.text, self.ids.email_reg.text, self.ids.pw_reg.text,
                             self.ids.pw_reg_2.text)
        pass

    @staticmethod
    def import_data(username_data, email_data, pass_data, pass_data2):
        postgres_insert_query = """INSERT INTO VoyagerKV_reg (USERNAME, EMAIL_ADDRESS, PASSWORD, 
        PASSWORD_VERIFICATION) VALUES (%s,%s,%s,%s) """
        record_to_insert = (username_data, email_data, pass_data, pass_data2)
        cur.execute(postgres_insert_query, record_to_insert,)
        conn.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into VoyagerKV_reg table")
        pass


sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(RegScreen(name='reg'))


class VoyagerMain(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Amber'  # theme color
        self.theme_cls.primary_hue = '900'  # theme hue
        self.theme_cls.theme_style = 'Dark'  # theme mode
        screen = Builder.load_string(screen_manager)
        return screen


if __name__ == '__main__':
    app = VoyagerMain()
    app.run()
