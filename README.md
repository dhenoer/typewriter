# Typewriter

Use typewriter style while sending text to terminal screen.

Mode / effect available:
* ltr : left to right as default, 
* rtl : right to left, and 
* scatter : for scattered print

## Usage

### print

`Typewriter.print(*arg, **kwarg)`

argument specified:

* `*arg` : similar to built-in print function
* `**kwarg` : 
    * similar to built-in print function, 
    * `mode = 'ltr'|'rtl'|'scatter'`


### input

`Typewriter.input(prompt, **kwarg)`

argument specified:

* `prompt` : similar to built-in input function
* `**kwarg` : include:
    * `mode = 'ltr'|'rtl'|'scatter'`

    
## Example
    
    import typewriter
    
    tw = typewriter.Typewriter
    
    tw.print('Hari Ulang Tahun')
    tw.print('================', mode='rtl')
    tw.print()

    while True:
        nama = tw.input('Nama: ', mode='ltr')
        lahir = tw.input('Tanggal Lahir (tgl/bln/thn): ')
        tgl, bln, thn = map(int, lahir.split('/'))
        # inputan tgl/bln/thn perlu validasi

        hariLahir = dt.date(thn, bln, tgl)
        hariIni = dt.date.today()
        hariUltah = dt.date(hariIni.year, bln, tgl)

        dLahir = hariIni - hariLahir
        dUltah = hariUltah - hariLahir
        umur = hariIni.year - hariLahir.year
        lewatHari = dLahir - dUltah

        tw.print(f'Apa kabar {nama}?', mode='scatter')
        tw.print(f'Ulang tahun kamu yang ke {umur}', end=' ')
        if dLahir > dUltah:
            tw.print(f'sudah lewat {lewatHari.days} hari. Selamat ya..')
        else:
            tw.print(f'masih {abs(lewatHari.days)} hari lagi..')

        print()
        q = tw.input('Tekan [Enter] untuk lagi', mode='rtl')
        if q != '':
            break
    
    
