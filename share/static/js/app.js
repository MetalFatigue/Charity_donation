document.addEventListener("DOMContentLoaded", function() {
  /**
   * HomePage - Help section
   */
  class Help {
    constructor($el) {
      this.$el = $el;
      this.$buttonsContainer = $el.querySelector(".help--buttons");
      this.$slidesContainers = $el.querySelectorAll(".help--slides");
      this.currentSlide = this.$buttonsContainer.querySelector(".active").parentElement.dataset.id;
      this.init();
    }

    init() {
      this.events();
    }

    events() {
      /**
       * Slide buttons
       */
      this.$buttonsContainer.addEventListener("click", e => {
        if (e.target.classList.contains("btn")) {
          this.changeSlide(e);
        }
      });

      /**
       * Pagination buttons
       */
      this.$el.addEventListener("click", e => {
        if (e.target.classList.contains("btn") && e.target.parentElement.parentElement.classList.contains("help--slides-pagination")) {
          this.changePage(e);
        }
      });
    }

    changeSlide(e) {
      e.preventDefault();
      const $btn = e.target;

      // Buttons Active class change
      [...this.$buttonsContainer.children].forEach(btn => btn.firstElementChild.classList.remove("active"));
      $btn.classList.add("active");

      // Current slide
      this.currentSlide = $btn.parentElement.dataset.id;

      // Slides active class change
      this.$slidesContainers.forEach(el => {
        el.classList.remove("active");

        if (el.dataset.id === this.currentSlide) {
          el.classList.add("active");
        }
      });
    }

    /**
     * TODO: callback to page change event
     */
    changePage(e) {
      e.preventDefault();
      const page = e.target.dataset.page;

      console.log(page);
    }
  }
  const helpSection = document.querySelector(".help");
  if (helpSection !== null) {
    new Help(helpSection);
  }

  /**
   * Form Select
   */
  class FormSelect {
    constructor($el) {
      this.$el = $el;
      this.options = [...$el.children];
      this.init();
    }

    init() {
      this.createElements();
      this.addEvents();
      this.$el.parentElement.removeChild(this.$el);
    }

    createElements() {
      // Input for value
      this.valueInput = document.createElement("input");
      this.valueInput.type = "text";
      this.valueInput.name = this.$el.name;

      // Dropdown container
      this.dropdown = document.createElement("div");
      this.dropdown.classList.add("dropdown");

      // List container
      this.ul = document.createElement("ul");

      // All list options
      this.options.forEach((el, i) => {
        const li = document.createElement("li");
        li.dataset.value = el.value;
        li.innerText = el.innerText;

        if (i === 0) {
          // First clickable option
          this.current = document.createElement("div");
          this.current.innerText = el.innerText;
          this.dropdown.appendChild(this.current);
          this.valueInput.value = el.value;
          li.classList.add("selected");
        }

        this.ul.appendChild(li);
      });

      this.dropdown.appendChild(this.ul);
      this.dropdown.appendChild(this.valueInput);
      this.$el.parentElement.appendChild(this.dropdown);
    }

    addEvents() {
      this.dropdown.addEventListener("click", e => {
        const target = e.target;
        this.dropdown.classList.toggle("selecting");

        // Save new value only when clicked on li
        if (target.tagName === "LI") {
          this.valueInput.value = target.dataset.value;
          this.current.innerText = target.innerText;
        }
      });
    }
  }
  document.querySelectorAll(".form-group--dropdown select").forEach(el => {
    new FormSelect(el);
  });

  /**
   * Hide elements when clicked on document
   */
  document.addEventListener("click", function(e) {
    const target = e.target;
    const tagName = target.tagName;

    if (target.classList.contains("dropdown")) return false;

    if (tagName === "LI" && target.parentElement.parentElement.classList.contains("dropdown")) {
      return false;
    }

    if (tagName === "DIV" && target.parentElement.classList.contains("dropdown")) {
      return false;
    }

    document.querySelectorAll(".form-group--dropdown .dropdown").forEach(el => {
      el.classList.remove("selecting");
    });
  });

  /**
   * Switching between form steps
   */
  class FormSteps {
    constructor(form) {
      this.$form = form;
      this.$next = form.querySelectorAll(".next-step");
      this.$prev = form.querySelectorAll(".prev-step");
      this.$step = form.querySelector(".form--steps-counter span");
      this.currentStep = 1;

      this.$stepInstructions = form.querySelectorAll(".form--steps-instructions p");
      const $stepForms = form.querySelectorAll("form > div");
      this.slides = [...this.$stepInstructions, ...$stepForms];

      this.init();
    }

    /**
     * Init all methods
     */
    init() {
      this.events();
      this.updateForm();
    }

    /**
     * All events that are happening in form
     */
    events() {
      // Next step
      this.$next.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep++;
          if(this.currentStep===2)
            {
            if (picked_checkboxes().length > 0){this.updateForm(); show_id()}
            else {this.currentStep--;}
            }

          if(this.currentStep===3) {this.updateForm()}
          if(this.currentStep===4) {this.updateForm()}
          if(this.currentStep===5) {donation_summary(); this.updateForm()}
          if(this.currentStep===6) {}
        });
      });

      // Previous step
      this.$prev.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep--;
          this.updateForm();
          if (this.currentStep == 1){
            console.log("test")
            console.log(document.querySelector('div#institutions'))
            document.querySelector('div#institutions').querySelectorAll("div").forEach(div => {div.remove()})

          }

        });
      });

      // Form submit
      this.$form.querySelector("form").addEventListener("submit", e => this.submit(e));
    }

    /**
     * Update form front-end
     * Show next or previous section etc.
     */
    updateForm() {
      this.$step.innerText = this.currentStep;

      // TODO: Validation

      this.slides.forEach(slide => {
        slide.classList.remove("active");

        if (slide.dataset.step == this.currentStep) {
          slide.classList.add("active");
        }
      });

      this.$stepInstructions[0].parentElement.parentElement.hidden = this.currentStep >= 6;
      this.$step.parentElement.hidden = this.currentStep >= 6;

      // TODO: get data from inputs and show them in summary
    }

    /**
     * Submit form
     *
     * TODO: validation, send data to server
     */
    submit(e) {
      e.preventDefault();
      this.currentStep++;
      this.updateForm();
    }
  }
  const form = document.querySelector(".form--steps");
  if (form !== null) {
    new FormSteps(form);
  }

});

  /**
   * Create URL with checked categories ids
   * Return list of institutions depend on categories ids
   */

  function show_id(event)
  {
    const h = document.querySelector('#institutions')
    var ids = picked_checkboxes();
    var params = new URLSearchParams();
    ids.forEach(id => params.append("id", id))
    var address = '/get_institution_by_category?'+ params.toString();
    fetch(address)
        .then(response => response.json())
        .then(institutions => institutions.forEach(institution => create_form_step_3(institution)));

  }
   /**
   * Return list of checked categories ids
   */

  function picked_checkboxes()
  {
      var picked_checkbox = document.querySelectorAll('input[type="checkbox"]:checked');
      var ids = [];
      picked_checkbox.forEach(box => ids.push(box.value));
      console.log(ids);
      return ids;
  }

  /**
   * Create Form step 3
   */

function create_form_step_3(institution)
  {
  const type_names = {
      1: 'Fundacja',
      2: 'Organizacja Pozarządowa',
      3: 'Lokalna Zbiórka'
  }

  let div = document.querySelector('#institutions');
  let button = div.querySelector('div.form-group--buttons');

  const maindiv = document.createElement("div")
  maindiv.setAttribute("class", "form-group form-group--checkbox");
  maindiv.setAttribute('id', 'single-institution');
  div.insertBefore(maindiv, button)

  const label = document.createElement("label")
  maindiv.appendChild(label)

  const input = document.createElement("input")
  input.setAttribute("id", "institution_radio_checkbox")
  input.setAttribute("type", "radio")
  input.setAttribute("name", "institution")
  input.setAttribute("value", institution.pk)
  input.setAttribute("institution_name", institution.fields.name)
  label.appendChild(input)

  const span1 = document.createElement("span")
  span1.setAttribute("class", "checkbox radio")
  label.appendChild(span1)

  const span2 = document.createElement("span")
  span2.setAttribute("class", "description")
  label.appendChild(span2)

  const div1 = document.createElement("div")
  div1.setAttribute("class", "title")
  div1.innerHTML = `${type_names[institution.fields.type]} "${institution.fields.name}"`
  span2.appendChild(div1)

  const div2 = document.createElement("div")
  div2.setAttribute("class", "subtitle")
  div2.innerHTML = `Cel i misja: ${institution.fields.description}`
  span2.appendChild(div2)
}

  /**
   * Create Form step 5
   */

  function donation_summary()
  {
    const address = document.querySelector("[name='address']").value
    const li1 = document.createElement("li")
    li1.innerHTML= address
    document.querySelector("ul#address-list").appendChild(li1)

    const city = document.querySelector("[name='city']").value
    const li2 = document.createElement("li")
    li2.innerHTML= city
    document.querySelector("ul#address-list").appendChild(li2)

    const zip_code = document.querySelector("[name='zip_code']").value
    const li3 = document.createElement("li")
    li3.innerHTML= zip_code
    document.querySelector("ul#address-list").appendChild(li3)

    const phone_number = document.querySelector("[name='phone_number']").value
    const li4 = document.createElement("li")
    li4.innerHTML= phone_number
    document.querySelector("ul#address-list").appendChild(li4)

    const pick_up_date = document.querySelector("[name='pick_up_date']")
    console.log(pick_up_date)
    const li5 = document.createElement("li")
    li5.innerHTML = pick_up_date.value
    document.querySelector("ul#pick-up-list").appendChild(li5)

    const pick_up_time = document.querySelector("[name='pick_up_time']")
    console.log(pick_up_time)
    const li6 = document.createElement("li")
    li6.innerHTML = pick_up_time.value
    document.querySelector("ul#pick-up-list").appendChild(li6)

    const pick_up_comment = document.querySelector("[name='pick_up_comment']")
    console.log(pick_up_comment)
    const li7 = document.createElement("li")
    li7.innerHTML = pick_up_comment.value
    document.querySelector("ul#pick-up-list").appendChild(li7)

    const picked_quantity = document.getElementById("bags").value
    const span1 =  document.getElementById('picked_quantity')
    span1.textContent = `Ilość przekazywanych worków ${picked_quantity}`

    const picked_institution = document.getElementById("institution_radio_checkbox").getAttribute("institution_name")
    const span2 = document.getElementById('picked_institution')
    span2.textContent = `Dla ${picked_institution}`
  }