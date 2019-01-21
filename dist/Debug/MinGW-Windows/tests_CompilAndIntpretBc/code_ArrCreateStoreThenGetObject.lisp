($ (setObj! c (newarray(6) ))
   (getObj! c)(dup) (iastore (1)(100))
              (dup) (iastore (2)(200))
   (setObj! r (newarray(12) ))
   (getObj! r)(dup) (iastore (1)(1000))
              (dup) (iastore (2)(2000))

   (set! b (7))
   (print b)
   (getObj! c) (dup) (iastore (1)(100.10))
)


