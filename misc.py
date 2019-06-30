from contextlib import redirect_stdout
import io

x =True
f = io.StringIO()
with redirect_stdout(f):
    if x ==True:
        print(f"ASDSD{11}")
    print('foobar')
    print(12)
    x  = input("dsadadasdad")
#rint('Got stdout: "{0}"'.format(f.getvalue()))

print(f'Got stdout: "{f.getvalue()}"')



# from IPython.utils.io import Tee
# from contextlib import closing
#
# print('This is not in the output file.')
#
# with closing(Tee("outputfile.log", "w", channel="stdout")) as outputstream:
#     print('This is written to the output file and the console.')
#     # raise Exception('The file "outputfile.log" is closed anyway.')
# print('This is not written to the output file.')
#
# # Output on console:
# # This is not in the output file.
# # This is written to the output file and the console.
# # This is not written to the output file.
#
# # Content of file outputfile.txt:
# # This is written to the output file and the console.