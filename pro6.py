# text to handwriting
import pywhatkit as pw
txt = """python is a simple and easy language.
 yug is here ."""""
#pw.text_to_handwriting(txt,[0,0,138])
pw.text_to_handwriting(txt, "pywhatkit.png",[0, 0, 0])