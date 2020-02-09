1.
sudo gedit /etc/X11/Xresources
replace everything with this (take a backup of the original if you wish):
```
Xft.hinting: true
Xft.autohint: false
Xft.rgba: rgb
Xft.lcdfilter: lcddefault
Xft.hintstyle: hintslight
```
2.
sudo gedit /etc/fonts/local.conf
paste this:
```
<?xml version="1.0"?>    
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">   
<fontconfig>    
<match target="font" >    
<edit mode="assign" name="autohint" >    
<bool>false</bool>
</edit>    
</match>    
<match target="font" >    
<edit mode="assign" name="rgba" >    
<const>rgb</const>
</edit>    
</match>    
<match target="font" >    
<edit mode="assign" name="hinting" >    
<bool>true</bool>
</edit>    
</match>    
<match target="font" >    
<edit mode="assign" name="hintstyle" >    
<const>hintslight</const>
</edit>    
</match>    
<match target="font" >    
<edit mode="assign" name="antialias" >    
<bool>true</bool>
</edit>    
</match>    
<match target="font" >    
<edit mode="assign" name="lcdfilter" >    
<const>lcddefault</const>
</edit>    
</match>    
</fontconfig>  
```
