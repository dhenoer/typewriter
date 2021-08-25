# Typewriter

Use typewriter style while sending text to terminal screen.

Mode / effect available:
* ltr : left to right as default, 
* rtl : right to left, and 
* scatter : for scattered print

## Usage

    Typewriter.print(*arg, **kwarg)
    *arg : similar to built-in print function 
    **kwarg: similar to built-in print function 
    mode = 'ltr'|'rtl'|'scatter'
    
    Typewriter.input(str, **kwarg)
    

    import typewriter
    
    tw = typewriter.Typewriter
    
    #start print default
    tw.print('Hello world')
    name = tw.input('Enter your name')
    
    #print scattered
    tw.print('Hello', name, 'where will you go?', mode='scatter')
    tw.print('Don\'t forget to turn around after 10 steps')
    
    #print right right to left
    
    
