# Triple D Columbus (beginner)
Hi, I'm Guy Fieri, and we're rolling out looking for America's greatest diners, drive-ins, and dives.

https://triple-d-columbus.chall.pwnoh.io

## Solution
If we access the website and take a look at the page source, we find the following section with the flag:
```html
  <!-- Contact Section -->
  <div class="w3-container w3-padding-64" id="contact">
    <h1>Contact</h1><br>
    <p>There is no contact set up yet because the resturant is still being built! Please send us a message to be added to our nesletter and to stay up to date!</p>
    <p class="w3-text-blue-grey w3-large"><b>You can send us a message here:</b></p>
    <form action="https://www.foodnetwork.com/fn-dish/chefs/2019/7/guy-fieri-shares-the-laws-of-flavortown" target="_blank">
      <p><input class="w3-input w3-padding-16" type="text" placeholder="Name" required name="Name"></p>
      <p><input class="w3-input w3-padding-16" type="datetime-local" placeholder="Date and time" required name="date" value="2020-11-16T20:00"></p>
      <p><input class="w3-input w3-padding-16" type="text" placeholder="Message \ Special requirements" required name="Message"></p>
      <p><button class="w3-button w3-light-grey w3-section" type="submit">SEND MESSAGE</button></p>
      <p hidden>bctf{In$pecT_eLemEnt_Is_prEttY_c00L_ayE?}</p>
    </form>
  </div>
```