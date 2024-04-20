import { defineStore } from "pinia";

export const useStore = defineStore('store', {
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
          },
          auth: {
            user_id: null,
            token: null
          }
    }),
    getters: {
        isAuthenticated: (state) => {
         return state.auth.token ? true : false 
        }
    },
    actions: {
      reserve(booking) {
        this.reservation.numberOfSeats = booking.numberOfSeats
        this.reservation.origin = booking.origin
        this.reservation.destination = booking.destination
      }
    },
    
})