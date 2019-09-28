const listAmenities = {};
const listStates = {};
const listCities = {};

$(function () {
  $('div.amenities li input').change(
    function () {
      if ($(this).is(':checked')) {
        listAmenities[($(this).attr('data-id'))] = $(this).attr('data-name');
        $('div.amenities h4').text(Object.values(listAmenities).join(', '));
        console.log('checked', $(this).attr('data-name'));
      } else {
        delete listAmenities[($(this).attr('data-id'))];
        $('div.amenities h4').text(Object.values(listAmenities).join(', '));
        console.log('un-checked', $(this).attr('data-name'));
      }
    });

  $.getJSON('http://0.0.0.0:5001/api/v1/status/', (data) => {
    if (data.status === 'OK') {
      $('DIV#api_status').addClass('available');
    } else {
      $('DIV#api_status').removeClass('available');
    }
  });

  $('button').click(() =>
    data = { amenities: Object.keys(listAmenities), 
	     states: Object.keys(listStates),
             cities: Object.keys(listCities) };
    $.ajax('http://0.0.0.0:5001/api/v1/places_search', {
      data: JSON.stringify(data),
      contentType: 'application/json',
      type: 'POST',
      success: data => {
        $('section.places').empty();
        for (const place of data) {
          const template = `<article>

      <div class="title">

        <h2>${place.name}</h2>

        <div class="price_by_night">

    $${place.price_by_night}

        </div>
      </div>
      <div class="information">
        <div class="max_guest">
    <i class="fa fa-users fa-3x" aria-hidden="true"></i>

    <br />

    ${place.max_guest} Guests

        </div>
        <div class="number_rooms">
    <i class="fa fa-bed fa-3x" aria-hidden="true"></i>

    <br />

    ${place.number_rooms} Bedrooms
        </div>
        <div class="number_bathrooms">
    <i class="fa fa-bath fa-3x" aria-hidden="true"></i>

    <br />

    ${place.number_bathrooms} Bathroom

        </div>
      </div>

      <!-- **********************
     USER
     **********************  -->

      <div class="description">

        ${place.description}

      </div>

    </article> <!-- End 1 PLACE Article -->`;
          $('section.places').append(template);
        }
      }
    }));

  $('div.locations li input').change(
    function () {
      if ($(this).is(':checked')) {
        listStates[($(this).attr('data-id'))] = $(this).attr('data-name');
        $('div.locations h4').text(Object.values(listStates).join(', '));
        console.log('checked', $(this).attr('data-name'));
      } else {
        delete listStates[($(this).attr('data-id'))];
        $('div.locations h4').text(Object.values(listStates).join(', '));
        console.log('un-checked', $(this).attr('data-name'));
      }
    });
  
   $('div.locations li input li input').change(
    function () {
      if ($(this).is(':checked')) {
        listCities[($(this).attr('data-id'))] = $(this).attr('data-name');
        $('div.locations h4').text(Object.values(listCities).join(', '));
        console.log('checked', $(this).attr('data-name'));
      } else {
        delete listCities[($(this).attr('data-id'))];
        $('div.locations h4').text(Object.values(listCities).join(', '));
        console.log('un-checked', $(this).attr('data-name'));
      }
    });
  
});