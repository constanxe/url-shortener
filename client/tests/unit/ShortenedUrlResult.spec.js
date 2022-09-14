import {shallowMount} from '@vue/test-utils'
import ShortenedUrlResult from '@/components/ShortenedUrlResult.vue'

Object.assign(navigator, {
  clipboard: {writeText: jest.fn()}
})

describe('ShortenedUrlResult.vue', () => {
  let wrapper
  let shortenedUrl = 'http://localhost:3000/qwe123'

  const getWrapper = () => shallowMount(ShortenedUrlResult, {
    propsData: {shortenedUrl}
  })

  beforeEach(() => wrapper = getWrapper())

  it('copies props.shortenedUrl when button clicked', () => {
    wrapper.find('button').trigger('click')

    expect(navigator.clipboard.writeText).toHaveBeenCalledWith(shortenedUrl)
  })

  describe('displays content if props.shortenedUrl passed', () => {
    const wrapperMatchesSnapshot = () => expect(wrapper).toMatchSnapshot()

    it('renders props.shortenedUrl when passed', () => {
      expect(wrapper.find(`a[href="${shortenedUrl}"]`).exists()).toBeTruthy()
      expect(wrapper.text()).toMatch('Shortened URL: ' + shortenedUrl)
      wrapperMatchesSnapshot()
    })

    it('does not show content when props.shortenedUrl empty', () => {
      shortenedUrl = ''
      wrapper = getWrapper()

      expect(wrapper.find('a').exists()).toBeFalsy()
      expect(wrapper.text()).toEqual(shortenedUrl)
      wrapperMatchesSnapshot()
    })
  })
})
