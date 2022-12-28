<template>
  <div>
    <modal-dialog
      title="Author Form"
      ref="authorFormModal"
      btn-ok-text="Salvar"
      @ok="okButton()">
      <div class="row">
        <div class="col-12">
          <label for="author-name">Nome:</label>
          <input type="text" id="author-name" class="form-control" maxlength="150" v-model="authorInstance.name">
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <label for="author-about">Sobre:</label>
          <textarea id="author-about" class="form-control" v-model="authorInstance.about"></textarea>
        </div>
      </div>
    </modal-dialog>
    <modal-dialog
      title="Author Form"
      ref="authorFormResponseModal"
      btn-ok-text="Fechar"
      :btn-cancel-visible="false"
      @ok="$refs.authorFormResponseModal.hide()">
      <div v-if="responseStatus===201">Author's data was saved</div>
      <div v-else-if="responseStatus && responseStatus!==201">Error... this system may need a doctor</div>
    </modal-dialog>
  </div>
</template>

<script>
import ModalDialog from '@/components/Modal.vue'
import { axiosAPI } from '@/axios'

export default {
  name: 'AuthorForm',
  props: ['author'],
  emits: ['update-authors'],
  components: {
    ModalDialog
  },
  data () {
    return {
      authorInstance: {
        id: null,
        name: '',
        about: ''
      },
      responseStatus: null
    }
  },

  methods: {
    saveInstance () {
      if (!this.authorInstance.id) {
        axiosAPI.post(`/authors/`, this.authorInstance).then((response) => {
          this.responseStatus = response.status
          if (response.status === 201) {
            this.$emit('update-authors')
            this.hide()
            this.showFormResponse()
          }
        })
      } else {
        axiosAPI.put(`/authors/${this.authorInstance.id}/`, this.authorInstance).then((response) => {
          this.responseStatus = response.status
          if (response.status === 200) {
            // emit update object
          }
        })
      }
    },

    hide () {
      this.$refs.authorFormModal.hide()
    },
    show () {
      this.$refs.authorFormModal.show()
    },
    showFormResponse () {
      this.$refs.authorFormResponseModal.show()
    },
    hideFormResponse () {
      this.$refs.authorFormResponseModal.hide()
    },

    okButton () {
      this.saveInstance()
    }
  }
}
</script>