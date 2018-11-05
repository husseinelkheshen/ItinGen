import Vue from 'vue'
import ItinGen from '@/components/ItinGen'

describe('ItinGen.vue', () => {
  const Constructor = Vue.extend(ItinGen)
  const vm = new Constructor().$mount()

  it('should render the correct header', () => {
    expect(vm.$el.querySelector('.header h1').textContent)
      .toEqual('Itinerary Generator')
  })

  it('should render the generate button', () => {
    expect(vm.$el.querySelector('.generate button').textContent)
      .toEqual('Generate')
  })

  it('should render the map', () => {
    expect(vm.$el.querySelector('.app div'))
      .contains('.vue-map-container')
  })

})
