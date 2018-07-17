
#include <X11/Xlib.h>
#include <X11/Xutil.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>


void click(Display *display, int button);
void coords(Display *display, int *x, int *y);
void move(Display *display, int x, int y);
void move_to(Display *display, int x, int y);
void pixel_color(Display *display, int x, int y, XColor *color);
