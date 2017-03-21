#!usr/bin/perl
@makata=("Makanan");
print"Isi awal dari array = @makata\n";
print"Masukkan kata = ";
$kata=<STDIN>;
print"\n";
push(@makata, $kata);
print"Isi array sekarang = @makata\n";
pop(@makata);
print"Isi array sekarang setelah di pop = @makata\n";
