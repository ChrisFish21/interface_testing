
# -*- coding: utf8 -*-

import remi.gui as gui
from remi.gui import *
from remi import start, App


class untitled(App):
    def __init__(self, *args, **kwargs):
        if not 'editing_mode' in kwargs.keys():
            super(untitled, self).__init__(*args, static_file_path='./res/')

    def idle(self):
        #idle function called every update cycle
        pass
    
    def main(self):
        return untitled.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        base = Widget()
        base.attributes.update({"class":"Widget","editor_constructor":"()","editor_varname":"base","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Widget"})
        base.style.update({"margin":"0px","width":"98%","height":"98%","top":"1%","left":"1%","position":"absolute","overflow":"auto","border-style":"solid"})
        lower_hor_cont = Widget()
        lower_hor_cont.attributes.update({"class":"Widget","editor_constructor":"()","editor_varname":"lower_hor_cont","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Widget"})
        lower_hor_cont.style.update({"margin":"0px","width":"100%","height":"20%","top":"80%","left":"0%","position":"absolute","overflow":"auto","border-style":"solid"})
        status_housing = Widget()
        status_housing.attributes.update({"class":"Widget","editor_constructor":"()","editor_varname":"status_housing","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Widget"})
        status_housing.style.update({"margin":"0px","width":"40%","height":"100%","position":"absolute","overflow":"auto","border-style":"solid"})
        lower_hor_cont.append(status_housing,'status_housing')
        pan_housing = Widget()
        pan_housing.attributes.update({"class":"Widget","editor_constructor":"()","editor_varname":"pan_housing","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Widget"})
        pan_housing.style.update({"margin":"0px","width":"15%","height":"100%","left":"40%","position":"absolute","overflow":"auto","border-style":"solid"})
        pan_label = Label('PAN')
        pan_label.attributes.update({"class":"Label","editor_constructor":"('PAN')","editor_varname":"pan_label","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Label"})
        pan_label.style.update({"margin":"0px","width":"100px","height":"30px","top":"20px","left":"20px","position":"absolute","overflow":"auto"})
        pan_housing.append(pan_label,'pan_label')
        pan_left_img = Image('left30x.png')
        pan_left_img.attributes.update({"class":"Image","src":"left30x.png","editor_constructor":"('left30x.png')","editor_varname":"pan_left_img","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Image"})
        pan_left_img.style.update({"margin":"0px","width":"40%","height":"50%","top":"40%","left":"5%","position":"absolute","overflow":"auto"})
        pan_housing.append(pan_left_img,'pan_left_img')
        lower_hor_cont.append(pan_housing,'pan_housing')
        tilt_housing = Widget()
        tilt_housing.attributes.update({"class":"Widget","editor_constructor":"()","editor_varname":"tilt_housing","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Widget"})
        tilt_housing.style.update({"margin":"0px","width":"15%","height":"100%","left":"55%","position":"absolute","overflow":"auto","border-style":"solid"})
        tilt_label = Label('TILT')
        tilt_label.attributes.update({"class":"Label","editor_constructor":"('TILT')","editor_varname":"tilt_label","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Label"})
        tilt_label.style.update({"margin":"0px","width":"100px","height":"30px","top":"20px","left":"20px","position":"absolute","overflow":"auto"})
        tilt_housing.append(tilt_label,'tilt_label')
        lower_hor_cont.append(tilt_housing,'tilt_housing')
        zoom_housing = Widget()
        zoom_housing.attributes.update({"class":"Widget","editor_constructor":"()","editor_varname":"zoom_housing","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Widget"})
        zoom_housing.style.update({"margin":"0px","width":"15%","height":"100%","left":"70%","position":"absolute","overflow":"auto","border-style":"solid"})
        zoom_label = Label('ZOOM')
        zoom_label.attributes.update({"class":"Label","editor_constructor":"('ZOOM')","editor_varname":"zoom_label","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Label"})
        zoom_label.style.update({"margin":"0px","width":"100px","height":"30px","top":"20px","left":"20px","position":"absolute","overflow":"auto"})
        zoom_housing.append(zoom_label,'zoom_label')
        lower_hor_cont.append(zoom_housing,'zoom_housing')
        cam_set_housing = Widget()
        cam_set_housing.attributes.update({"class":"Widget","editor_constructor":"()","editor_varname":"cam_set_housing","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Widget"})
        cam_set_housing.style.update({"margin":"0px","width":"15%","height":"100%","left":"85%","position":"absolute","overflow":"auto","border-style":"solid"})
        cam_set_label = Label('CAMERA SETTINGS')
        cam_set_label.attributes.update({"class":"Label","editor_constructor":"('CAMERA SETTINGS')","editor_varname":"cam_set_label","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Label"})
        cam_set_label.style.update({"margin":"0px","width":"100px","height":"30px","top":"20px","left":"20px","position":"absolute","overflow":"auto"})
        cam_set_housing.append(cam_set_label,'cam_set_label')
        lower_hor_cont.append(cam_set_housing,'cam_set_housing')
        base.append(lower_hor_cont,'lower_hor_cont')
        top_hor_cont = Widget()
        top_hor_cont.attributes.update({"class":"Widget","editor_constructor":"()","editor_varname":"top_hor_cont","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Widget"})
        top_hor_cont.style.update({"margin":"0px","width":"100%","height":"20%","position":"absolute","overflow":"auto","border-style":"solid"})
        power_box = Widget()
        power_box.attributes.update({"class":"Widget","editor_constructor":"()","editor_varname":"power_box","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Widget"})
        power_box.style.update({"margin":"0px","width":"13%","height":"100%","position":"absolute","overflow":"hidden","border-style":"solid"})
        top_hor_cont.append(power_box,'power_box')
        current_alt_box = Widget()
        current_alt_box.attributes.update({"class":"Widget","editor_constructor":"()","editor_varname":"current_alt_box","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Widget"})
        current_alt_box.style.update({"margin":"0px","width":"20%","height":"100%","left":"13%","position":"absolute","overflow":"hidden","border-style":"solid"})
        top_hor_cont.append(current_alt_box,'current_alt_box')
        target_alt_box = Widget()
        target_alt_box.attributes.update({"class":"Widget","editor_constructor":"()","editor_varname":"target_alt_box","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Widget"})
        target_alt_box.style.update({"margin":"0px","width":"20%","height":"100%","left":"33%","position":"absolute","overflow":"auto","border-style":"solid"})
        top_hor_cont.append(target_alt_box,'target_alt_box')
        change_alt_box = Widget()
        change_alt_box.attributes.update({"class":"Widget","editor_constructor":"()","editor_varname":"change_alt_box","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Widget"})
        change_alt_box.style.update({"margin":"0px","width":"13%","height":"100%","left":"53%","position":"absolute","overflow":"hidden","border-style":"solid"})
        top_hor_cont.append(change_alt_box,'change_alt_box')
        turn_drone_box = Widget()
        turn_drone_box.attributes.update({"class":"Widget","editor_constructor":"()","editor_varname":"turn_drone_box","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Widget"})
        turn_drone_box.style.update({"margin":"0px","width":"20%","height":"100%","left":"66%","position":"absolute","overflow":"hidden","border-style":"solid"})
        top_hor_cont.append(turn_drone_box,'turn_drone_box')
        land_box = Widget()
        land_box.attributes.update({"class":"Widget","editor_constructor":"()","editor_varname":"land_box","editor_tag_type":"widget","editor_newclass":"False","editor_baseclass":"Widget"})
        land_box.style.update({"margin":"0px","width":"13%","height":"100%","position":"absolute","overflow":"auto","right":"0%","border-style":"solid"})
        top_hor_cont.append(land_box,'land_box')
        base.append(top_hor_cont,'top_hor_cont')
        base.children['lower_hor_cont'].children['pan_housing'].children['pan_left_img'].onclick.connect(self.onclick_pan_left_img)
        

        self.base = base
        return self.base
    
    def onclick_pan_left_img(self, emitter):
        pass



#Configuration
configuration = {'config_project_name': 'untitled', 'config_address': '0.0.0.0', 'config_port': 8081, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(untitled, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])
