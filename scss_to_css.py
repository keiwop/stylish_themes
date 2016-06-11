#! 	/usr/bin/env python3

from scss.namespace import Namespace
from scss.types import String
from scss import compiler
import glob
import os

def compile_scss():
	scss_list = glob.glob("./*.scss")
	print("\n\n\n\nSCSS_FILES:", scss_list)
	for scss_path in scss_list:
		css_path = scss_path.replace("scss", "css")
		print("\nscss path:", scss_path)
		print("css path:", css_path)
#		print("app path:", self.app_path)
#		asset_path = self.app_path + "/icons/assets/checkbox-checked_"
#		asset_path += os.path.basename(scss_path).split(".")[0] + ".svg"
		print("scss file:", os.path.basename(scss_path))
#		print("asset_path:", asset_path)
		
		namespace = Namespace()
#		namespace.set_variable("$asset_path", String(asset_path))
		css_data = compiler.compile_file(scss_path, namespace=namespace)
		print("css:", css_data)
		with open(css_path, "w") as css_file:
			css_file.write(css_data)

if __name__ == "__main__":
	compile_scss()
