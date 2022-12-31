<template>
  <div>
    <modal-dialog
      title="Author Form"
      ref="formModal"
      btn-ok-text="Salvar"
      @ok="saveInstance">
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
      ref="formResponseModal"
      btn-ok-text="Fechar"
      :btn-cancel-visible="false"
      @ok="$refs.formResponseModal.hide()">
      <div v-if="responseStatus===201">Author was created</div>
      <div v-else-if="responseStatus===200">Author's data was saved</div>
      <div v-else-if="responseStatus">Error... this system may need a doctor</div>
    </modal-dialog>
  </div>
</template>

<script>
import ModalDialog from '@/components/Modal.vue'
import FormMixin from '@/mixins/FormMixin';

export default {
  name: 'AuthorForm',
  mixins: [FormMixin],
  emits: ['update-authors'],
  props: ['authorLoad'],

  components: {
    ModalDialog
  },

  mounted () {
    this.formReset()
  },

  watch: {
    authorLoad (newValue) {
      if (newValue) {
        this.authorInstance = Object.assign({}, newValue)
      }
    }
  },

  computed: {
    loadedInstance () {
      return this.authorInstance
    }
  },

  data () {
    return {
      instanceName: 'authors',
      authorInstance: {},
      authorObjectModel: {
        id: null,
        name: '',
        about: ''
      }
    }
  },

  methods: {
    formReset () {
      this.authorInstance = Object.assign({}, this.authorObjectModel)
    }
  }
}
</script>