# LOST 1
<div align="center" style="font-size: smaller;">
<img width="940" height="898" alt="Challenge prompt: Lost 1" src="https://github.com/user-attachments/assets/48304c93-e98c-4f04-9f3d-1b2acb082790" />
</div>

## Log ID 2607225: Day 1

The prompt:
> I'm lost, please tell me where I am?\
> Flag format: ```wwf{51.945,59.402}```

## TL;DR
> Got a Street View screenshot with zero metadata.  
> AI misled me, Agoda helped me narrow it down to Nice, France.  
> Matched graffiti and landmarks to coordinates.  
> Flag: `wwf{43.688, 7.236}`

<div align="center" style="font-size: smaller;">
<img width="940" height="636" alt="Attached file: Screenshot_2025-03-29_164005.png" src="https://github.com/user-attachments/assets/b41568fd-473b-4a9f-896d-2fea573b267a" />
</div>

GeoGuessr challenge? I opened the file. It was *obviously* a screenshot of Google Maps Street View, thanks to the 2023 watermark and the wide-angle view. 

I started breaking it down:
- A **Y-shaped** intersection
- A **bridge crossing** with vertical railings
- **Vivid graffiti** under the bridge of a woman's face
- A **traffic light**, a **signboard**, and strong **European vibes™**

Naturally, I Exif'd it.\
Zero metadata. The image was clean. 

<div align="center" style="font-size: smaller;">
<img width="940" height="588" alt="Attempting to extract metadata using ExifInfo, which confirmed the image was scrubbed of EXIF data." src="https://github.com/user-attachments/assets/3ecb94d7-68c2-485c-a0f1-eba26e7f17ea" />
</div>

### **Next move:** Reverse image search. 

Google Lens AI said **Boulevard Gambetta** and **Avenue des Baumettes** intersection. 

Source? Trust me bro.

<div align="center" style="font-size: smaller;">
<img width="940" height="640" alt="The Incorrect AI Overview in question" src="https://github.com/user-attachments/assets/8163234f-1d02-4209-83c2-8c659f91e9be" />
</div>

Spoiler: It was wrong.

## Log ID 270725: Day 2
I gave it another shot, this time focusing on the visuals. I ran it through Google Lens once again.

<div align="center" style="font-size: smaller;">
<img width="940" height="588" alt="The same image discovered via Google Lens on booking.com, but visual match found on Agoda during the CTF." src="https://github.com/user-attachments/assets/ab4f9332-5043-4ef4-bb45-6df96f6d2675" />
</div>

**Jackpot.**\
I found a match. On **Agoda**.

<div align="center" style="font-size: smaller;"> 
<img width="900" height="1200" alt="The similar image on Agoda" src="https://github.com/user-attachments/assets/040afea4-9662-4998-9e9d-b289f2710cae" />
</div>

[Agoda Listing](https://www.agoda.com/en-gb/fabron-h33056264/hotel/nice-fr.html) 

<div align="center" style="font-size: smaller;">
<img width="940" height="588" alt="Agoda page, not sponsored, that cracked the case." src="https://github.com/user-attachments/assets/86f2cdc3-d402-4135-a5de-f68c43b19822" />
</div>

The hotel? Fabron, Nice. We're close.

<div align="center" style="font-size: smaller;"> 
<img width="940" height="588" alt="Agoda's map view showing the location of the hotel." src="https://github.com/user-attachments/assets/6fb2c3ec-7c12-47c7-81e1-9a9ed78fcaf6" />
</div>

No Street View on Agoda. So I hit up Google Maps and started scanning Fabron.

Eventually, I found a street that matched the screenshot's vibe.

<div align="center" style="font-size: smaller;">
<img width="940" height="588" alt="Y shaped road" src="https://github.com/user-attachments/assets/c732ac5e-805b-4f89-909f-cda18aa50122" />
</div>

I dropped the yellow guy onto the map and time-traveled to 2023.
Perfect match. Graffiti, bridge, traffic lights, all of it.

<div align="center" style="font-size: smaller;">
<img width="940" height="588" alt="The graffiti. The railings. The Y-intersection. Nailed it." src="https://github.com/user-attachments/assets/af66599a-c78f-4802-8ddb-e81ed068c6d7" />
</div>

[Google Maps Link](https://maps.app.goo.gl/usrec8FEryJPZTop7)

Grabbed the coordinates straight from the URL:
```43.6880866, 7.2366215```

First guess?
```wwf{43.688, 7.237}```\
No.

Second try?
```wwf{43.688, 7.236}```\
Submitted it. Nothing. I thought it failed. Only later did I realize I had solved it.

<div align="center" style="font-size: smaller;">
<img width="940" height="760" alt="Suffering from success" src="https://github.com/user-attachments/assets/e19c4d15-51ee-4b48-b0b2-b7366abd7985" />
</div>

## **Flag:** `wwf{43.688, 7.236}`
  
## Takeaways:
- Don't trust AI blindly

## 🫶 Shoutouts:
- Much love to my teammates [@Aravind](https://github.com/Aravind-808) and [@Joshni](https://github.com/joshni86)
- Credits to [@vizer](https://github.com/vjz3r) for the challenge
- Also shoutout to Street View for giving me motion sickness
