# mathai
Decoder-only Transformer model trained to generate math

After training for a couple minutes, I inputted:
```
${
  mp2.1 $e |- ph $.
  mp2.2 $e |- ps $.
  mp2.3 $e |- ( ph -> ( ps -> ch ) ) $.
  mp2 $p |- ch $=
```
and it completed:
```
${
  mp2.1 $e |- ph $.
  mp2.2 $e |- ps $.
  mp2.3 $e |- ( ph -> ( ps -> ch ) ) $.
  mp2 $p |- ch $=
  mp2.51mp2.3 $e |- ( ph -> ps ) $.
    mp2r2.5 $e |- ( ph -> ( ps -> ps ) ) $.
  mp2.2 $p |- ( ph -> ps ) $.
  mp2r2.7 $e |- ( ( ph <-> ps ) -> ( et -> ps -> ps ) ). $.
  mp2an.2 $e |- ( ph ) $.
TosetRel 2 . 4  $e |- ( ph -> F e. SH ) $.
${
  mp2.2 $e |- ( ph -> F ps ) $.
  wl-el $.
  $d x $. V m i n 1  $p |- ( ph -> ps ) $.
  mp2a.2 $e |- ( ph -> ( ( ph /\ ps ) -> ps ) ) $=
  mp2.1 $e |- ( ph -> F Fn A ) $.
$}
```
