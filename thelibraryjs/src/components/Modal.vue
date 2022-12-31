<template>
  <div
    class="modal"
    tabindex="-1"
    ref="modalContainer"
    id="modal_container"
    :data-bs-backdrop="staticClosure ? 'static' : 'true'"
    :data-bs-keyboard="staticClosure ? 'false' : 'true'">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">{{ title }}</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <slot></slot>
        </div>
        <div class="modal-footer">
          <button
            type="button" class="btn btn-secondary" data-bs-dismiss="modal"
            @click="$emit('cancel')"
            v-if="btnCancelVisible">{{ btnCancelText }}</button>
          <button type="button" class="btn btn-primary" @click="$emit('ok')">{{ btnOkText }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Modal } from "bootstrap"
export default {
  name: 'ModalDialog',
  emits: ['ok', 'cancel'],
  props: {
    title: {
      type: String,
      required: true      
    },
    btnOkText: {
      type: String,
      default: 'OK'
    },
    btnCancelText: {
      type: String,
      default: 'Cancelar'
    },
    btnCancelVisible: {
      type: Boolean,
      default: true
    },
    staticClosure: {
      type: Boolean,
      default: true
    }
  },
  mounted () {
    this.modalObj = new Modal(this.$refs.modalContainer)
  },

  data () {
    return {
      modalObj: null,
    }
  },

  methods: {
    show () {
      this.modalObj.show()
    },
    hide () {
      this.modalObj.hide()
    }
  }
}
</script>
