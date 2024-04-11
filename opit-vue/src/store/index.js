import { defineStore } from "pinia";

export const useStore = defineStore('sotre', {
    state: () => ({
        cities: [
            { data: "Kampala", value: 'KLA' },
            { data: "Entebbe", value: 'EBB' },
            { data: "Mbarara", value: 'MBR' },
            { data: "Mukono", value: 'MKN' },
            { data: "Gulu", value: 'GLU' },
            { data: "Kotido", value: 'KTD' },
            { data: "Jinja", value: 'JJA' },
          ],
          reservation: {
            numberOfSeats: 1,
            origin: '',
            destination: ''
          }
    }),
    getter: {

    }

})