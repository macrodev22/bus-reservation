import axios from "axios";

const URL = 'http://localhost:5000/api'
const apiClient = axios.create({
    baseURL: URL,
    headers: {
        'Accept': 'application/json',
        'Content-Type' : 'application/json'
    }
})

export const makeReservation = (booking) => {

    return apiClient.post('/reservations', booking)
}

export const getReservations = () => {
    return apiClient.get('/reservations')
}

export const registerUser = (userDetails) => {
    return apiClient.post('/users', {
        type: 'registration',
        data: userDetails
    })
}

export const login = (userCredentials) => {
    return apiClient.post('/login', {
        ...userCredentials
    })
}

export const updateFare = (fareDetails) => {
    return apiClient.post('/fares', {
        type: 'update fare',
        data: fareDetails
    })
}

export const getFare = (fareDetails) => {
    return apiClient.get(`/fares/${fareDetails.origin}/${fareDetails.destination}`)
}


export default apiClient