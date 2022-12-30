
/**
 * * In the component:
 * - Must use a formModal with the form contents
 * - Must have a responseFormModal
 * - Must have a computed called loadedInstance that returns the data object instance or you also can just call it loadedInstance
 * - Can have "postValidate" and "postPrepare" methods and they will be called just before post request
 * - Must have a data called instanceName wich must match the endpoint name, as in '/books/' instaneName should be = 'books'
 * - Can have declared emit 'update-${this.instanceName}' as in 'update-books'
 */
import { axiosAPI } from '@/axios'

export default {
  data () {
    return {
      responseStatus: null
    }
  },

  methods: {
    saveInstance () {
      if (!this.instanceName) return ''
      if (typeof this.prepareFormData === 'function') {
        this.prepareFormData()
      }
      /** verify and exec the "validate function" */
      if (!this.loadedInstance.id) {
        axiosAPI.post(`/${this.instanceName}/`, this.loadedInstance).then((response) => {
          this.responseStatus = response.status
          if (response.status === 201) {
            // check if there is a configured emit with this name
            this.$emit(`update-${this.instanceName}`)
            this.hide()
            this.showFormResponse()
          }
        })
      } else {
        axiosAPI.put(`/${this.instanceName}/${this.loadedInstance.id}/`, this.loadedInstance).then((response) => {
          this.responseStatus = response.status
          if (response.status === 200) {
            // emit update object
          }
        })
      }
    },
  
    hide () {
      this.$refs.formModal.hide()
    },

    show () {
      this.$refs.formModal.show()
    },

    showFormResponse () {
      this.$refs.formResponseModal.show()
    },

    hideFormResponse () {
      this.$refs.formResponseModal.hide()
    },

    loadFile (event, fieldName) {
      let fileEl = event.target.files[0]
      let fileRead = new FileReader()
      fileRead.addEventListener("load", () => {
        this.loadedInstance[fieldName] = fileRead.result.toString().replace('data:', '').replace(/^.+,/, '')
      }, false)
      fileRead.readAsDataURL(fileEl)
    }
  }
}