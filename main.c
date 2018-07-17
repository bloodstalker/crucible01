
#include <stdio.h>
#include <inttypes.h>
#include <X11/Xlib.h>
#include <X11/Xutil.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

#include "autoclick.h"
#include "log.h"

int main (int argc, char** argv) {
  Display *display = XOpenDisplay(NULL);
  for (int i = 0; i < co_size; ++i) {
    //printf("x:%d--y:%d", co[i].x, co[i].y);
    move(display, co[i].x, co[i].y);
    move_to(display, co[i].x, co[i].y);
  }
  //printf("\n");
  XCloseDisplay(display);
  return 0;
}
