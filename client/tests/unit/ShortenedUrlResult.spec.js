import { shallowMount } from '@vue/test-utils'
import ShortenedUrlResult from '@/components/ShortenedUrlResult.vue'

Object.assign(navigator, {
  clipboard: {writeText: jest.fn()}
})

describe('ShortenedUrlResult.vue', () => {
  let wrapper
  let shortenedUrl = 'http://localhost:3000/qwe123'

  beforeEach(() => wrapper = shallowMount(ShortenedUrlResult, {
    propsData: {shortenedUrl}
  }))

  it('copies props.shortenedUrl when button clicked', () => {
    wrapper.find('button').trigger('click')

    expect(navigator.clipboard.writeText).toHaveBeenCalledWith(shortenedUrl)
  })

  describe('displays content if props.shortenedUrl passed', () => {
    it('renders props.shortenedUrl when passed', () => {
      expect(wrapper.find(`a[href="${shortenedUrl}"]`).exists()).toBeTruthy()
      expect(wrapper.text()).toMatch('Shortened URL: ' + shortenedUrl)
      expect(wrapper).toMatchSnapshot()
    })

    it('does not show content when props.shortenedUrl empty', () => {
      shortenedUrl = ''
      wrapper = shallowMount(ShortenedUrlResult, {
        propsData: {shortenedUrl}
      })

      expect(wrapper.find('a').exists()).toBeFalsy()
      expect(wrapper.text()).toEqual(shortenedUrl)
      expect(wrapper).toMatchSnapshot()
    })
  })
})
