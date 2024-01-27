class DynamicAdapt {
    constructor(type) {
        this.type = type;
    }

    init() {
        this.оbjects = [];
        this.daClassname = "_dynamic_adapt_";
        this.nodes = [...document.querySelectorAll("[data-da]")];
        this.nodes.forEach((node => {
            const data = node.dataset.da.trim();
            const dataArray = data.split(",");
            const оbject = {};
            оbject.element = node;
            оbject.parent = node.parentNode;
            оbject.destination = document.querySelector(`${dataArray[0].trim()}`);
            оbject.breakpoint = dataArray[1] ? dataArray[1].trim() : "767";
            оbject.place = dataArray[2] ? dataArray[2].trim() : "last";
            оbject.index = this.indexInParent(оbject.parent, оbject.element);
            this.оbjects.push(оbject);
        }));
        this.arraySort(this.оbjects);
        this.mediaQueries = this.оbjects.map((({breakpoint}) => `(${this.type}-width: ${breakpoint}px),${breakpoint}`)).filter(((item, index, self) => self.indexOf(item) === index));
        this.mediaQueries.forEach((media => {
            const mediaSplit = media.split(",");
            const matchMedia = window.matchMedia(mediaSplit[0]);
            const mediaBreakpoint = mediaSplit[1];
            const оbjectsFilter = this.оbjects.filter((({breakpoint}) => breakpoint === mediaBreakpoint));
            matchMedia.addEventListener("change", (() => {
                this.mediaHandler(matchMedia, оbjectsFilter);
            }));
            this.mediaHandler(matchMedia, оbjectsFilter);
        }));
    }

    mediaHandler(matchMedia, оbjects) {
        if (matchMedia.matches) оbjects.forEach((оbject => {
            this.moveTo(оbject.place, оbject.element, оbject.destination);
        })); else оbjects.forEach((({parent, element, index}) => {
            if (element.classList.contains(this.daClassname)) this.moveBack(parent, element, index);
        }));
    }

    moveTo(place, element, destination) {
        element.classList.add(this.daClassname);
        if (place === "last" || place >= destination.children.length) {
            destination.append(element);
            return;
        }
        if (place === "first") {
            destination.prepend(element);
            return;
        }
        destination.children[place].before(element);
    }

    moveBack(parent, element, index) {
        element.classList.remove(this.daClassname);
        if (parent.children[index] !== void 0) parent.children[index].before(element); else parent.append(element);
    }

    indexInParent(parent, element) {
        return [...parent.children].indexOf(element);
    }

    arraySort(arr) {
        if (this.type === "min") arr.sort(((a, b) => {
            if (a.breakpoint === b.breakpoint) {
                if (a.place === b.place) return 0;
                if (a.place === "first" || b.place === "last") return -1;
                if (a.place === "last" || b.place === "first") return 1;
                return 0;
            }
            return a.breakpoint - b.breakpoint;
        })); else {
            arr.sort(((a, b) => {
                if (a.breakpoint === b.breakpoint) {
                    if (a.place === b.place) return 0;
                    if (a.place === "first" || b.place === "last") return 1;
                    if (a.place === "last" || b.place === "first") return -1;
                    return 0;
                }
                return b.breakpoint - a.breakpoint;
            }));
            return;
        }
    }
}

const da = new DynamicAdapt("max");
da.init();
if (document.getElementById("calcDemo")) {
    const demo = document.getElementById("calcDemo"),
        range = document.getElementById("calcRange"),
        calcRadio1 = document.getElementById("radio-1"),
        calcRadio2 = document.getElementById("radio-2"),
        calcRadio3 = document.getElementById("radio-3"),
        calcRadio4 = document.getElementById("radio-4"),
        calcRadio5 = document.getElementById("radio-5");
    let calcList = document.getElementById("listCalc");
    const allPrice = document.querySelector(".response-calc__price");
    const selectContent = document.querySelectorAll(".quantity-calc__option");
    const radioCalc = document.querySelectorAll(".radios-calc__radio");
    demo.innerHTML = range.value;

    let material = calcRadio1.dataset.number;

    calcRadio1.addEventListener("input", (function () {
        radioCalc.forEach((radio => {
            if (radio.checked) {
                material = radio.dataset.number;
            }
        }));
        selectContent.forEach(((item, i) => {
            if (item.selected) allPrice.textContent = material * demo.value * item.textContent;
        }));
    }));

    calcRadio2.addEventListener("input", (function () {
        radioCalc.forEach((radio => {
            if (radio.checked) {
                material = radio.dataset.number;
            }
        }));
        selectContent.forEach(((item, i) => {
            if (item.selected) allPrice.textContent = material * demo.value * item.textContent;
        }));
    }));

    calcRadio3.addEventListener("input", (function () {
        radioCalc.forEach((radio => {
            if (radio.checked) {
                material = radio.dataset.number;
            }
        }));
        selectContent.forEach(((item, i) => {
            if (item.selected) allPrice.textContent = material * demo.value * item.textContent;
        }));
    }));

    calcRadio4.addEventListener("input", (function () {
        radioCalc.forEach((radio => {
            if (radio.checked) {
                material = radio.dataset.number;
            }
        }));
        selectContent.forEach(((item, i) => {
            if (item.selected) allPrice.textContent = material * demo.value * item.textContent;
        }));
    }));

    calcRadio5.addEventListener("input", (function () {
        radioCalc.forEach((radio => {
            if (radio.checked) {
                material = radio.dataset.number;
            }
        }));
        selectContent.forEach(((item, i) => {
            if (item.selected) allPrice.textContent = material * demo.value * item.textContent;
        }));
    }));

    range.addEventListener("input", (function () {
        demo.value = this.value;
        radioCalc.forEach((radio => {
            if (radio.checked) {
                material = radio.dataset.number;
            }
        }));
        selectContent.forEach(((item, i) => {
            if (item.selected) allPrice.textContent = material * this.value * item.textContent;
        }));
    }));

    calcList.addEventListener("change", function () {
        demo.value = this.value;
        radioCalc.forEach((radio => {
            if (radio.checked) {
                material = radio.dataset.number;
            }
        }));
        selectContent.forEach(((item, i) => {
            if (item.selected) allPrice.textContent = material * this.value * item.textContent;
        }));
    });

    demo.addEventListener("input", (e => {
        const regex = /^\d+$/;
        const inputValue = e.target.value;
        console.log('selectContent')
        if (!regex.test(inputValue)) e.target.value = ""; else {
            range.value = inputValue;
            radioCalc.forEach((radio => {
                if (radio.checked) {
                    material = radio.dataset.number;
                }
            }));
            selectContent.forEach(((item, i) => {
                if (item.selected) allPrice.textContent = material * inputValue * item.textContent;
            }));
        }
        if (inputValue > 100) e.target.value = "";
    }));
}