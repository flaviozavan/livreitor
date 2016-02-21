Livreitor
======

A set a tools for scanning physical books.
The final result is a PDF containing pictures of all pages.

### How to scan

1. Tape the book to a firm surface.

2. Find a decent webcam, I used a Logitech Pro 9000, and tape it somewhere firm
making sure the whole page fits in a single picture.

3. Calibrate the focus and other options. I used guvcview for this.

4. Capture all the images. One for each page, or one for each 2 pages if you find that the image quality is good enough.  Use capture.py, each time you press Return, a picture is saved. When Escape is pressed, the program stops. If you run it again, it will continue from where it left off.
- Example: ./capture.py -c 1 -w 1600 -h 1200 -s .75 out
- The scale parameter is only used on the preview
- -c 0 should work for most people
- If you mess up, don't worry, just keep taking the pictures
- I recommend using a remote control, so you don't have to reach for the keyboard all the time

5. Delete all bad pictures and/or take the missing. Sort the filenames lexicographically according to their order in the book, you may use any filename for this.

6. Run fix_names.sh, this will rename all images, getting rid of ocassional gaps and arbitraty names used for sorting.
- Example: ./fix_names.sh out

7. Create a ranges file, listing the page ranges where the book might have moved. Use the page numbers in the out directory. This is specially useful for the cover and when one side of the book gets too heavy when flipping the pages.
- An example is provided in example_ranges.txt.

8. Use calibrata.py and select all the request page corners.
- Example: example_ranges.txt out calibrated.txt

9. Use warp.py to warp and crop the pages properly.
- Example: ./warp.py calibrated.txt out warped

10. Use build_pdf.sh to create a PDF file.
- Example: ./build_pdf.sh warped book.pdf
