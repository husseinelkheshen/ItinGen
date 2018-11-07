import Vue from 'vue'
import ItinGen from '@/components/ItinGen'

describe('ItinGen.vue', () => {
  const Constructor = Vue.extend(ItinGen)
  const vm = new Constructor().$mount()

  it('should render the correct header', () => {
    expect(vm.$el.querySelector('.header h1').textContent)
      .toEqual('Itinerary Generator')
  })

  it('should render the map', () => {
    expect(vm.$el.querySelector('.app div'))
      .contains('.vue-map-container')
  })

  it('should display a location', () => {
    expect(vm.$el.querySelector('.app div'))
      .contains('.vue-map-marker')
  })

  it('should display a sidebar', () => {
    expect(vm.$el.querySelector('.app div'))
      .contains('.sidebar')
  })

  it('should display a login button', () => {
    expect(vm.$el.querySelector('.sidebar button').textContent)
      .toEqual('Login')
  })

  it('should display a sign up button', () => {
    expect(vm.$el.querySelector('sidebar button').textContent)
      .toEqual('Signup')
  })

  it('should display an itinerary', () => {
    expect(vm.$el.querySelector('sidebar div'))
      .containes('.itinerary')
  })

  it('should render the generate button', () => {
    expect(vm.$el.querySelector('.generate button').textContent)
      .toEqual('Generate')
  })

  it('should render the dislike button', () => {
    expect(vm.$el.querySelector('.dislike button').textContent)
      .toEqual('Dislike')
  })

  it('should render a save current itinerary button', () => {
    expect(vm.$el.querySelector('.save button').textContent)
      .toEqual('Save Current Itinerary')
  })

  it('should render a link to saved itineraries', () => {
    expect(vm.$el.querySelector('.saved button').textContent)
      .toEqual('View Saved Itineraries')
  })

})
