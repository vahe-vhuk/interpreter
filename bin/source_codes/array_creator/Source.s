	.file	"Source.cpp"
	.text
	.globl	make_int_array
	.type	make_int_array, @function
make_int_array:
.LFB12:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$32, %rsp
	movq	%rdi, -8(%rbp)
	movl	%esi, -12(%rbp)
	movl	%edx, -16(%rbp)
	movl	%ecx, -20(%rbp)
	movl	%r8d, -24(%rbp)
	movl	%r9d, -28(%rbp)
	movl	-28(%rbp), %r8d
	movl	-24(%rbp), %edi
	movl	-20(%rbp), %ecx
	movl	-16(%rbp), %edx
	movl	-12(%rbp), %esi
	movq	-8(%rbp), %rax
	movl	%r8d, %r9d
	movl	%edi, %r8d
	movq	%rax, %rdi
	call	_Z5makerIiEvPT_iiS0_S0_i
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE12:
	.size	make_int_array, .-make_int_array
	.globl	make_double_array
	.type	make_double_array, @function
make_double_array:
.LFB13:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$48, %rsp
	movq	%rdi, -8(%rbp)
	movl	%esi, -12(%rbp)
	movl	%edx, -16(%rbp)
	movsd	%xmm0, -24(%rbp)
	movsd	%xmm1, -32(%rbp)
	movl	%ecx, -36(%rbp)
	movl	-36(%rbp), %ecx
	movsd	-32(%rbp), %xmm0
	movq	-24(%rbp), %rdi
	movl	-16(%rbp), %edx
	movl	-12(%rbp), %esi
	movq	-8(%rbp), %rax
	movapd	%xmm0, %xmm1
	movq	%rdi, %xmm0
	movq	%rax, %rdi
	call	_Z5makerIdEvPT_iiS0_S0_i
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE13:
	.size	make_double_array, .-make_double_array
	.section	.text._Z5makerIiEvPT_iiS0_S0_i,"axG",@progbits,_Z5makerIiEvPT_iiS0_S0_i,comdat
	.weak	_Z5makerIiEvPT_iiS0_S0_i
	.type	_Z5makerIiEvPT_iiS0_S0_i, @function
_Z5makerIiEvPT_iiS0_S0_i:
.LFB14:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$48, %rsp
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movl	%ecx, -36(%rbp)
	movl	%r8d, -40(%rbp)
	movl	%r9d, -44(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L4
.L5:
	movl	-4(%rbp), %eax
	cltq
	leaq	0(,%rax,4), %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movl	$0, (%rax)
	addl	$1, -4(%rbp)
.L4:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L5
	cmpl	$0, -36(%rbp)
	je	.L20
	cmpl	$10, -44(%rbp)
	ja	.L3
	movl	-44(%rbp), %eax
	leaq	0(,%rax,4), %rdx
	leaq	.L9(%rip), %rax
	movl	(%rdx,%rax), %eax
	cltq
	leaq	.L9(%rip), %rdx
	addq	%rdx, %rax
	jmp	*%rax
	.section	.rodata._Z5makerIiEvPT_iiS0_S0_i,"aG",@progbits,_Z5makerIiEvPT_iiS0_S0_i,comdat
	.align 4
	.align 4
.L9:
	.long	.L19-.L9
	.long	.L18-.L9
	.long	.L17-.L9
	.long	.L16-.L9
	.long	.L15-.L9
	.long	.L14-.L9
	.long	.L13-.L9
	.long	.L12-.L9
	.long	.L11-.L9
	.long	.L10-.L9
	.long	.L8-.L9
	.section	.text._Z5makerIiEvPT_iiS0_S0_i,"axG",@progbits,_Z5makerIiEvPT_iiS0_S0_i,comdat
.L19:
	movl	-36(%rbp), %ecx
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %esi
	movq	-24(%rbp), %rax
	movq	%rax, %rdi
	call	_Z12simple_arrayIiEvPT_iiS0_
	jmp	.L3
.L18:
	movl	-36(%rbp), %ecx
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %esi
	movq	-24(%rbp), %rax
	movq	%rax, %rdi
	call	_Z14diagonal_arrayIiEvPT_iiS0_
	jmp	.L3
.L17:
	movl	-36(%rbp), %ecx
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %esi
	movq	-24(%rbp), %rax
	movq	%rax, %rdi
	call	_Z18top_diagonal_arrayIiEvPT_iiS0_
	jmp	.L3
.L16:
	movl	-36(%rbp), %ecx
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %esi
	movq	-24(%rbp), %rax
	movq	%rax, %rdi
	call	_Z22top_and_diagonal_arrayIiEvPT_iiS0_
	jmp	.L3
.L15:
	movl	-36(%rbp), %ecx
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %esi
	movq	-24(%rbp), %rax
	movq	%rax, %rdi
	call	_Z21bottom_diagonal_arrayIiEvPT_iiS0_
	jmp	.L3
.L14:
	movl	-36(%rbp), %ecx
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %esi
	movq	-24(%rbp), %rax
	movq	%rax, %rdi
	call	_Z25bottom_and_diagonal_arrayIiEvPT_iiS0_
	jmp	.L3
.L13:
	movl	-36(%rbp), %ecx
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %esi
	movq	-24(%rbp), %rax
	movq	%rax, %rdi
	call	_Z18sec_diagonal_arrayIiEvPT_iiS0_
	jmp	.L3
.L12:
	movl	-36(%rbp), %ecx
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %esi
	movq	-24(%rbp), %rax
	movq	%rax, %rdi
	call	_Z22top_sec_diagonal_arrayIiEvPT_iiS0_
	jmp	.L3
.L11:
	movl	-36(%rbp), %ecx
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %esi
	movq	-24(%rbp), %rax
	movq	%rax, %rdi
	call	_Z26top_and_sec_diagonal_arrayIiEvPT_iiS0_
	jmp	.L3
.L10:
	movl	-36(%rbp), %ecx
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %esi
	movq	-24(%rbp), %rax
	movq	%rax, %rdi
	call	_Z25bottom_sec_diagonal_arrayIiEvPT_iiS0_
	jmp	.L3
.L8:
	movl	-36(%rbp), %ecx
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %esi
	movq	-24(%rbp), %rax
	movq	%rax, %rdi
	call	_Z29bottom_and_sec_diagonal_arrayIiEvPT_iiS0_
	jmp	.L3
.L20:
	nop
.L3:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE14:
	.size	_Z5makerIiEvPT_iiS0_S0_i, .-_Z5makerIiEvPT_iiS0_S0_i
	.section	.text._Z5makerIdEvPT_iiS0_S0_i,"axG",@progbits,_Z5makerIdEvPT_iiS0_S0_i,comdat
	.weak	_Z5makerIdEvPT_iiS0_S0_i
	.type	_Z5makerIdEvPT_iiS0_S0_i, @function
_Z5makerIdEvPT_iiS0_S0_i:
.LFB15:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$64, %rsp
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movsd	%xmm0, -40(%rbp)
	movsd	%xmm1, -48(%rbp)
	movl	%ecx, -52(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L22
.L23:
	movl	-4(%rbp), %eax
	cltq
	leaq	0(,%rax,8), %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	pxor	%xmm0, %xmm0
	movsd	%xmm0, (%rax)
	addl	$1, -4(%rbp)
.L22:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L23
	pxor	%xmm0, %xmm0
	ucomisd	-40(%rbp), %xmm0
	jp	.L24
	pxor	%xmm0, %xmm0
	ucomisd	-40(%rbp), %xmm0
	je	.L39
.L24:
	cmpl	$10, -52(%rbp)
	ja	.L21
	movl	-52(%rbp), %eax
	leaq	0(,%rax,4), %rdx
	leaq	.L28(%rip), %rax
	movl	(%rdx,%rax), %eax
	cltq
	leaq	.L28(%rip), %rdx
	addq	%rdx, %rax
	jmp	*%rax
	.section	.rodata._Z5makerIdEvPT_iiS0_S0_i,"aG",@progbits,_Z5makerIdEvPT_iiS0_S0_i,comdat
	.align 4
	.align 4
.L28:
	.long	.L38-.L28
	.long	.L37-.L28
	.long	.L36-.L28
	.long	.L35-.L28
	.long	.L34-.L28
	.long	.L33-.L28
	.long	.L32-.L28
	.long	.L31-.L28
	.long	.L30-.L28
	.long	.L29-.L28
	.long	.L27-.L28
	.section	.text._Z5makerIdEvPT_iiS0_S0_i,"axG",@progbits,_Z5makerIdEvPT_iiS0_S0_i,comdat
.L38:
	movq	-40(%rbp), %rsi
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %ecx
	movq	-24(%rbp), %rax
	movq	%rsi, %xmm0
	movl	%ecx, %esi
	movq	%rax, %rdi
	call	_Z12simple_arrayIdEvPT_iiS0_
	jmp	.L21
.L37:
	movq	-40(%rbp), %rsi
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %ecx
	movq	-24(%rbp), %rax
	movq	%rsi, %xmm0
	movl	%ecx, %esi
	movq	%rax, %rdi
	call	_Z14diagonal_arrayIdEvPT_iiS0_
	jmp	.L21
.L36:
	movq	-40(%rbp), %rsi
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %ecx
	movq	-24(%rbp), %rax
	movq	%rsi, %xmm0
	movl	%ecx, %esi
	movq	%rax, %rdi
	call	_Z18top_diagonal_arrayIdEvPT_iiS0_
	jmp	.L21
.L35:
	movq	-40(%rbp), %rsi
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %ecx
	movq	-24(%rbp), %rax
	movq	%rsi, %xmm0
	movl	%ecx, %esi
	movq	%rax, %rdi
	call	_Z22top_and_diagonal_arrayIdEvPT_iiS0_
	jmp	.L21
.L34:
	movq	-40(%rbp), %rsi
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %ecx
	movq	-24(%rbp), %rax
	movq	%rsi, %xmm0
	movl	%ecx, %esi
	movq	%rax, %rdi
	call	_Z21bottom_diagonal_arrayIdEvPT_iiS0_
	jmp	.L21
.L33:
	movq	-40(%rbp), %rsi
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %ecx
	movq	-24(%rbp), %rax
	movq	%rsi, %xmm0
	movl	%ecx, %esi
	movq	%rax, %rdi
	call	_Z25bottom_and_diagonal_arrayIdEvPT_iiS0_
	jmp	.L21
.L32:
	movq	-40(%rbp), %rsi
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %ecx
	movq	-24(%rbp), %rax
	movq	%rsi, %xmm0
	movl	%ecx, %esi
	movq	%rax, %rdi
	call	_Z18sec_diagonal_arrayIdEvPT_iiS0_
	jmp	.L21
.L31:
	movq	-40(%rbp), %rsi
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %ecx
	movq	-24(%rbp), %rax
	movq	%rsi, %xmm0
	movl	%ecx, %esi
	movq	%rax, %rdi
	call	_Z22top_sec_diagonal_arrayIdEvPT_iiS0_
	jmp	.L21
.L30:
	movq	-40(%rbp), %rsi
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %ecx
	movq	-24(%rbp), %rax
	movq	%rsi, %xmm0
	movl	%ecx, %esi
	movq	%rax, %rdi
	call	_Z26top_and_sec_diagonal_arrayIdEvPT_iiS0_
	jmp	.L21
.L29:
	movq	-40(%rbp), %rsi
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %ecx
	movq	-24(%rbp), %rax
	movq	%rsi, %xmm0
	movl	%ecx, %esi
	movq	%rax, %rdi
	call	_Z25bottom_sec_diagonal_arrayIdEvPT_iiS0_
	jmp	.L21
.L27:
	movq	-40(%rbp), %rsi
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %ecx
	movq	-24(%rbp), %rax
	movq	%rsi, %xmm0
	movl	%ecx, %esi
	movq	%rax, %rdi
	call	_Z29bottom_and_sec_diagonal_arrayIdEvPT_iiS0_
	jmp	.L21
.L39:
	nop
.L21:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE15:
	.size	_Z5makerIdEvPT_iiS0_S0_i, .-_Z5makerIdEvPT_iiS0_S0_i
	.section	.text._Z12simple_arrayIiEvPT_iiS0_,"axG",@progbits,_Z12simple_arrayIiEvPT_iiS0_,comdat
	.weak	_Z12simple_arrayIiEvPT_iiS0_
	.type	_Z12simple_arrayIiEvPT_iiS0_, @function
_Z12simple_arrayIiEvPT_iiS0_:
.LFB16:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movl	%ecx, -36(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L41
.L42:
	movl	-4(%rbp), %eax
	cltq
	leaq	0(,%rax,4), %rdx
	movq	-24(%rbp), %rax
	addq	%rax, %rdx
	movl	-36(%rbp), %eax
	movl	%eax, (%rdx)
	addl	$1, -4(%rbp)
.L41:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L42
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE16:
	.size	_Z12simple_arrayIiEvPT_iiS0_, .-_Z12simple_arrayIiEvPT_iiS0_
	.section	.text._Z14diagonal_arrayIiEvPT_iiS0_,"axG",@progbits,_Z14diagonal_arrayIiEvPT_iiS0_,comdat
	.weak	_Z14diagonal_arrayIiEvPT_iiS0_
	.type	_Z14diagonal_arrayIiEvPT_iiS0_, @function
_Z14diagonal_arrayIiEvPT_iiS0_:
.LFB17:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movl	%ecx, -36(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L44
.L45:
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	movl	%eax, %edx
	movl	-4(%rbp), %eax
	addl	%edx, %eax
	cltq
	leaq	0(,%rax,4), %rdx
	movq	-24(%rbp), %rax
	addq	%rax, %rdx
	movl	-36(%rbp), %eax
	movl	%eax, (%rdx)
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L44:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L45
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE17:
	.size	_Z14diagonal_arrayIiEvPT_iiS0_, .-_Z14diagonal_arrayIiEvPT_iiS0_
	.section	.text._Z18top_diagonal_arrayIiEvPT_iiS0_,"axG",@progbits,_Z18top_diagonal_arrayIiEvPT_iiS0_,comdat
	.weak	_Z18top_diagonal_arrayIiEvPT_iiS0_
	.type	_Z18top_diagonal_arrayIiEvPT_iiS0_, @function
_Z18top_diagonal_arrayIiEvPT_iiS0_:
.LFB18:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movl	%ecx, -36(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L47
.L50:
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	addl	$1, %eax
	movl	%eax, -8(%rbp)
	jmp	.L48
.L49:
	movl	-4(%rbp), %edx
	movl	-8(%rbp), %eax
	addl	%edx, %eax
	cltq
	leaq	0(,%rax,4), %rdx
	movq	-24(%rbp), %rax
	addq	%rax, %rdx
	movl	-36(%rbp), %eax
	movl	%eax, (%rdx)
	addl	$1, -8(%rbp)
.L48:
	movl	-8(%rbp), %eax
	cmpl	-32(%rbp), %eax
	jl	.L49
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L47:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L50
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE18:
	.size	_Z18top_diagonal_arrayIiEvPT_iiS0_, .-_Z18top_diagonal_arrayIiEvPT_iiS0_
	.section	.text._Z22top_and_diagonal_arrayIiEvPT_iiS0_,"axG",@progbits,_Z22top_and_diagonal_arrayIiEvPT_iiS0_,comdat
	.weak	_Z22top_and_diagonal_arrayIiEvPT_iiS0_
	.type	_Z22top_and_diagonal_arrayIiEvPT_iiS0_, @function
_Z22top_and_diagonal_arrayIiEvPT_iiS0_:
.LFB19:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movl	%ecx, -36(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L52
.L55:
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	movl	%eax, -8(%rbp)
	jmp	.L53
.L54:
	movl	-4(%rbp), %edx
	movl	-8(%rbp), %eax
	addl	%edx, %eax
	cltq
	leaq	0(,%rax,4), %rdx
	movq	-24(%rbp), %rax
	addq	%rax, %rdx
	movl	-36(%rbp), %eax
	movl	%eax, (%rdx)
	addl	$1, -8(%rbp)
.L53:
	movl	-8(%rbp), %eax
	cmpl	-32(%rbp), %eax
	jl	.L54
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L52:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L55
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE19:
	.size	_Z22top_and_diagonal_arrayIiEvPT_iiS0_, .-_Z22top_and_diagonal_arrayIiEvPT_iiS0_
	.section	.text._Z21bottom_diagonal_arrayIiEvPT_iiS0_,"axG",@progbits,_Z21bottom_diagonal_arrayIiEvPT_iiS0_,comdat
	.weak	_Z21bottom_diagonal_arrayIiEvPT_iiS0_
	.type	_Z21bottom_diagonal_arrayIiEvPT_iiS0_, @function
_Z21bottom_diagonal_arrayIiEvPT_iiS0_:
.LFB20:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movl	%ecx, -36(%rbp)
	movl	-32(%rbp), %eax
	movl	%eax, -4(%rbp)
	jmp	.L57
.L60:
	movl	$0, -8(%rbp)
	jmp	.L58
.L59:
	movl	-4(%rbp), %edx
	movl	-8(%rbp), %eax
	addl	%edx, %eax
	cltq
	leaq	0(,%rax,4), %rdx
	movq	-24(%rbp), %rax
	addq	%rax, %rdx
	movl	-36(%rbp), %eax
	movl	%eax, (%rdx)
	addl	$1, -8(%rbp)
.L58:
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	cmpl	%eax, -8(%rbp)
	jl	.L59
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L57:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L60
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE20:
	.size	_Z21bottom_diagonal_arrayIiEvPT_iiS0_, .-_Z21bottom_diagonal_arrayIiEvPT_iiS0_
	.section	.text._Z25bottom_and_diagonal_arrayIiEvPT_iiS0_,"axG",@progbits,_Z25bottom_and_diagonal_arrayIiEvPT_iiS0_,comdat
	.weak	_Z25bottom_and_diagonal_arrayIiEvPT_iiS0_
	.type	_Z25bottom_and_diagonal_arrayIiEvPT_iiS0_, @function
_Z25bottom_and_diagonal_arrayIiEvPT_iiS0_:
.LFB21:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movl	%ecx, -36(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L62
.L65:
	movl	$0, -8(%rbp)
	jmp	.L63
.L64:
	movl	-4(%rbp), %edx
	movl	-8(%rbp), %eax
	addl	%edx, %eax
	cltq
	leaq	0(,%rax,4), %rdx
	movq	-24(%rbp), %rax
	addq	%rax, %rdx
	movl	-36(%rbp), %eax
	movl	%eax, (%rdx)
	addl	$1, -8(%rbp)
.L63:
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	cmpl	%eax, -8(%rbp)
	jle	.L64
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L62:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L65
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE21:
	.size	_Z25bottom_and_diagonal_arrayIiEvPT_iiS0_, .-_Z25bottom_and_diagonal_arrayIiEvPT_iiS0_
	.section	.text._Z18sec_diagonal_arrayIiEvPT_iiS0_,"axG",@progbits,_Z18sec_diagonal_arrayIiEvPT_iiS0_,comdat
	.weak	_Z18sec_diagonal_arrayIiEvPT_iiS0_
	.type	_Z18sec_diagonal_arrayIiEvPT_iiS0_, @function
_Z18sec_diagonal_arrayIiEvPT_iiS0_:
.LFB22:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movl	%ecx, -36(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L67
.L68:
	movl	-4(%rbp), %edx
	movl	-32(%rbp), %eax
	addl	%edx, %eax
	leal	-1(%rax), %ecx
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	movl	%eax, %edx
	movl	%ecx, %eax
	subl	%edx, %eax
	cltq
	leaq	0(,%rax,4), %rdx
	movq	-24(%rbp), %rax
	addq	%rax, %rdx
	movl	-36(%rbp), %eax
	movl	%eax, (%rdx)
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L67:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L68
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE22:
	.size	_Z18sec_diagonal_arrayIiEvPT_iiS0_, .-_Z18sec_diagonal_arrayIiEvPT_iiS0_
	.section	.text._Z22top_sec_diagonal_arrayIiEvPT_iiS0_,"axG",@progbits,_Z22top_sec_diagonal_arrayIiEvPT_iiS0_,comdat
	.weak	_Z22top_sec_diagonal_arrayIiEvPT_iiS0_
	.type	_Z22top_sec_diagonal_arrayIiEvPT_iiS0_, @function
_Z22top_sec_diagonal_arrayIiEvPT_iiS0_:
.LFB23:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movl	%ecx, -36(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L70
.L73:
	movl	$0, -8(%rbp)
	jmp	.L71
.L72:
	movl	-4(%rbp), %edx
	movl	-8(%rbp), %eax
	addl	%edx, %eax
	cltq
	leaq	0(,%rax,4), %rdx
	movq	-24(%rbp), %rax
	addq	%rax, %rdx
	movl	-36(%rbp), %eax
	movl	%eax, (%rdx)
	addl	$1, -8(%rbp)
.L71:
	movl	-32(%rbp), %eax
	leal	-1(%rax), %ecx
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	movl	%eax, %edx
	movl	%ecx, %eax
	subl	%edx, %eax
	cmpl	%eax, -8(%rbp)
	jl	.L72
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L70:
	movl	-32(%rbp), %eax
	subl	$1, %eax
	imull	-28(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L73
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE23:
	.size	_Z22top_sec_diagonal_arrayIiEvPT_iiS0_, .-_Z22top_sec_diagonal_arrayIiEvPT_iiS0_
	.section	.text._Z26top_and_sec_diagonal_arrayIiEvPT_iiS0_,"axG",@progbits,_Z26top_and_sec_diagonal_arrayIiEvPT_iiS0_,comdat
	.weak	_Z26top_and_sec_diagonal_arrayIiEvPT_iiS0_
	.type	_Z26top_and_sec_diagonal_arrayIiEvPT_iiS0_, @function
_Z26top_and_sec_diagonal_arrayIiEvPT_iiS0_:
.LFB24:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movl	%ecx, -36(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L75
.L78:
	movl	$0, -8(%rbp)
	jmp	.L76
.L77:
	movl	-4(%rbp), %edx
	movl	-8(%rbp), %eax
	addl	%edx, %eax
	cltq
	leaq	0(,%rax,4), %rdx
	movq	-24(%rbp), %rax
	addq	%rax, %rdx
	movl	-36(%rbp), %eax
	movl	%eax, (%rdx)
	addl	$1, -8(%rbp)
.L76:
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	movl	%eax, %edx
	movl	-32(%rbp), %eax
	subl	%edx, %eax
	cmpl	%eax, -8(%rbp)
	jl	.L77
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L75:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L78
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE24:
	.size	_Z26top_and_sec_diagonal_arrayIiEvPT_iiS0_, .-_Z26top_and_sec_diagonal_arrayIiEvPT_iiS0_
	.section	.text._Z25bottom_sec_diagonal_arrayIiEvPT_iiS0_,"axG",@progbits,_Z25bottom_sec_diagonal_arrayIiEvPT_iiS0_,comdat
	.weak	_Z25bottom_sec_diagonal_arrayIiEvPT_iiS0_
	.type	_Z25bottom_sec_diagonal_arrayIiEvPT_iiS0_, @function
_Z25bottom_sec_diagonal_arrayIiEvPT_iiS0_:
.LFB25:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movl	%ecx, -36(%rbp)
	movl	-32(%rbp), %eax
	movl	%eax, -4(%rbp)
	jmp	.L80
.L83:
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	movl	%eax, %edx
	movl	-32(%rbp), %eax
	subl	%edx, %eax
	movl	%eax, -8(%rbp)
	jmp	.L81
.L82:
	movl	-4(%rbp), %edx
	movl	-8(%rbp), %eax
	addl	%edx, %eax
	cltq
	leaq	0(,%rax,4), %rdx
	movq	-24(%rbp), %rax
	addq	%rax, %rdx
	movl	-36(%rbp), %eax
	movl	%eax, (%rdx)
	addl	$1, -8(%rbp)
.L81:
	movl	-8(%rbp), %eax
	cmpl	-32(%rbp), %eax
	jl	.L82
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L80:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L83
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE25:
	.size	_Z25bottom_sec_diagonal_arrayIiEvPT_iiS0_, .-_Z25bottom_sec_diagonal_arrayIiEvPT_iiS0_
	.section	.text._Z29bottom_and_sec_diagonal_arrayIiEvPT_iiS0_,"axG",@progbits,_Z29bottom_and_sec_diagonal_arrayIiEvPT_iiS0_,comdat
	.weak	_Z29bottom_and_sec_diagonal_arrayIiEvPT_iiS0_
	.type	_Z29bottom_and_sec_diagonal_arrayIiEvPT_iiS0_, @function
_Z29bottom_and_sec_diagonal_arrayIiEvPT_iiS0_:
.LFB26:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movl	%ecx, -36(%rbp)
	movl	-32(%rbp), %eax
	movl	%eax, -4(%rbp)
	jmp	.L85
.L88:
	movl	-32(%rbp), %eax
	leal	-1(%rax), %ecx
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	movl	%eax, %edx
	movl	%ecx, %eax
	subl	%edx, %eax
	movl	%eax, -8(%rbp)
	jmp	.L86
.L87:
	movl	-4(%rbp), %edx
	movl	-8(%rbp), %eax
	addl	%edx, %eax
	cltq
	leaq	0(,%rax,4), %rdx
	movq	-24(%rbp), %rax
	addq	%rax, %rdx
	movl	-36(%rbp), %eax
	movl	%eax, (%rdx)
	addl	$1, -8(%rbp)
.L86:
	movl	-8(%rbp), %eax
	cmpl	-32(%rbp), %eax
	jl	.L87
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L85:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L88
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE26:
	.size	_Z29bottom_and_sec_diagonal_arrayIiEvPT_iiS0_, .-_Z29bottom_and_sec_diagonal_arrayIiEvPT_iiS0_
	.section	.text._Z12simple_arrayIdEvPT_iiS0_,"axG",@progbits,_Z12simple_arrayIdEvPT_iiS0_,comdat
	.weak	_Z12simple_arrayIdEvPT_iiS0_
	.type	_Z12simple_arrayIdEvPT_iiS0_, @function
_Z12simple_arrayIdEvPT_iiS0_:
.LFB27:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movsd	%xmm0, -40(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L90
.L91:
	movl	-4(%rbp), %eax
	cltq
	leaq	0(,%rax,8), %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movsd	-40(%rbp), %xmm0
	movsd	%xmm0, (%rax)
	addl	$1, -4(%rbp)
.L90:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L91
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE27:
	.size	_Z12simple_arrayIdEvPT_iiS0_, .-_Z12simple_arrayIdEvPT_iiS0_
	.section	.text._Z14diagonal_arrayIdEvPT_iiS0_,"axG",@progbits,_Z14diagonal_arrayIdEvPT_iiS0_,comdat
	.weak	_Z14diagonal_arrayIdEvPT_iiS0_
	.type	_Z14diagonal_arrayIdEvPT_iiS0_, @function
_Z14diagonal_arrayIdEvPT_iiS0_:
.LFB28:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movsd	%xmm0, -40(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L93
.L94:
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	movl	%eax, %edx
	movl	-4(%rbp), %eax
	addl	%edx, %eax
	cltq
	leaq	0(,%rax,8), %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movsd	-40(%rbp), %xmm0
	movsd	%xmm0, (%rax)
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L93:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L94
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE28:
	.size	_Z14diagonal_arrayIdEvPT_iiS0_, .-_Z14diagonal_arrayIdEvPT_iiS0_
	.section	.text._Z18top_diagonal_arrayIdEvPT_iiS0_,"axG",@progbits,_Z18top_diagonal_arrayIdEvPT_iiS0_,comdat
	.weak	_Z18top_diagonal_arrayIdEvPT_iiS0_
	.type	_Z18top_diagonal_arrayIdEvPT_iiS0_, @function
_Z18top_diagonal_arrayIdEvPT_iiS0_:
.LFB29:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movsd	%xmm0, -40(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L96
.L99:
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	addl	$1, %eax
	movl	%eax, -8(%rbp)
	jmp	.L97
.L98:
	movl	-4(%rbp), %edx
	movl	-8(%rbp), %eax
	addl	%edx, %eax
	cltq
	leaq	0(,%rax,8), %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movsd	-40(%rbp), %xmm0
	movsd	%xmm0, (%rax)
	addl	$1, -8(%rbp)
.L97:
	movl	-8(%rbp), %eax
	cmpl	-32(%rbp), %eax
	jl	.L98
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L96:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L99
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE29:
	.size	_Z18top_diagonal_arrayIdEvPT_iiS0_, .-_Z18top_diagonal_arrayIdEvPT_iiS0_
	.section	.text._Z22top_and_diagonal_arrayIdEvPT_iiS0_,"axG",@progbits,_Z22top_and_diagonal_arrayIdEvPT_iiS0_,comdat
	.weak	_Z22top_and_diagonal_arrayIdEvPT_iiS0_
	.type	_Z22top_and_diagonal_arrayIdEvPT_iiS0_, @function
_Z22top_and_diagonal_arrayIdEvPT_iiS0_:
.LFB30:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movsd	%xmm0, -40(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L101
.L104:
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	movl	%eax, -8(%rbp)
	jmp	.L102
.L103:
	movl	-4(%rbp), %edx
	movl	-8(%rbp), %eax
	addl	%edx, %eax
	cltq
	leaq	0(,%rax,8), %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movsd	-40(%rbp), %xmm0
	movsd	%xmm0, (%rax)
	addl	$1, -8(%rbp)
.L102:
	movl	-8(%rbp), %eax
	cmpl	-32(%rbp), %eax
	jl	.L103
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L101:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L104
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE30:
	.size	_Z22top_and_diagonal_arrayIdEvPT_iiS0_, .-_Z22top_and_diagonal_arrayIdEvPT_iiS0_
	.section	.text._Z21bottom_diagonal_arrayIdEvPT_iiS0_,"axG",@progbits,_Z21bottom_diagonal_arrayIdEvPT_iiS0_,comdat
	.weak	_Z21bottom_diagonal_arrayIdEvPT_iiS0_
	.type	_Z21bottom_diagonal_arrayIdEvPT_iiS0_, @function
_Z21bottom_diagonal_arrayIdEvPT_iiS0_:
.LFB31:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movsd	%xmm0, -40(%rbp)
	movl	-32(%rbp), %eax
	movl	%eax, -4(%rbp)
	jmp	.L106
.L109:
	movl	$0, -8(%rbp)
	jmp	.L107
.L108:
	movl	-4(%rbp), %edx
	movl	-8(%rbp), %eax
	addl	%edx, %eax
	cltq
	leaq	0(,%rax,8), %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movsd	-40(%rbp), %xmm0
	movsd	%xmm0, (%rax)
	addl	$1, -8(%rbp)
.L107:
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	cmpl	%eax, -8(%rbp)
	jl	.L108
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L106:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L109
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE31:
	.size	_Z21bottom_diagonal_arrayIdEvPT_iiS0_, .-_Z21bottom_diagonal_arrayIdEvPT_iiS0_
	.section	.text._Z25bottom_and_diagonal_arrayIdEvPT_iiS0_,"axG",@progbits,_Z25bottom_and_diagonal_arrayIdEvPT_iiS0_,comdat
	.weak	_Z25bottom_and_diagonal_arrayIdEvPT_iiS0_
	.type	_Z25bottom_and_diagonal_arrayIdEvPT_iiS0_, @function
_Z25bottom_and_diagonal_arrayIdEvPT_iiS0_:
.LFB32:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movsd	%xmm0, -40(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L111
.L114:
	movl	$0, -8(%rbp)
	jmp	.L112
.L113:
	movl	-4(%rbp), %edx
	movl	-8(%rbp), %eax
	addl	%edx, %eax
	cltq
	leaq	0(,%rax,8), %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movsd	-40(%rbp), %xmm0
	movsd	%xmm0, (%rax)
	addl	$1, -8(%rbp)
.L112:
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	cmpl	%eax, -8(%rbp)
	jle	.L113
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L111:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L114
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE32:
	.size	_Z25bottom_and_diagonal_arrayIdEvPT_iiS0_, .-_Z25bottom_and_diagonal_arrayIdEvPT_iiS0_
	.section	.text._Z18sec_diagonal_arrayIdEvPT_iiS0_,"axG",@progbits,_Z18sec_diagonal_arrayIdEvPT_iiS0_,comdat
	.weak	_Z18sec_diagonal_arrayIdEvPT_iiS0_
	.type	_Z18sec_diagonal_arrayIdEvPT_iiS0_, @function
_Z18sec_diagonal_arrayIdEvPT_iiS0_:
.LFB33:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movsd	%xmm0, -40(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L116
.L117:
	movl	-4(%rbp), %edx
	movl	-32(%rbp), %eax
	addl	%edx, %eax
	leal	-1(%rax), %ecx
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	movl	%eax, %edx
	movl	%ecx, %eax
	subl	%edx, %eax
	cltq
	leaq	0(,%rax,8), %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movsd	-40(%rbp), %xmm0
	movsd	%xmm0, (%rax)
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L116:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L117
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE33:
	.size	_Z18sec_diagonal_arrayIdEvPT_iiS0_, .-_Z18sec_diagonal_arrayIdEvPT_iiS0_
	.section	.text._Z22top_sec_diagonal_arrayIdEvPT_iiS0_,"axG",@progbits,_Z22top_sec_diagonal_arrayIdEvPT_iiS0_,comdat
	.weak	_Z22top_sec_diagonal_arrayIdEvPT_iiS0_
	.type	_Z22top_sec_diagonal_arrayIdEvPT_iiS0_, @function
_Z22top_sec_diagonal_arrayIdEvPT_iiS0_:
.LFB34:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movsd	%xmm0, -40(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L119
.L122:
	movl	$0, -8(%rbp)
	jmp	.L120
.L121:
	movl	-4(%rbp), %edx
	movl	-8(%rbp), %eax
	addl	%edx, %eax
	cltq
	leaq	0(,%rax,8), %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movsd	-40(%rbp), %xmm0
	movsd	%xmm0, (%rax)
	addl	$1, -8(%rbp)
.L120:
	movl	-32(%rbp), %eax
	leal	-1(%rax), %ecx
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	movl	%eax, %edx
	movl	%ecx, %eax
	subl	%edx, %eax
	cmpl	%eax, -8(%rbp)
	jl	.L121
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L119:
	movl	-32(%rbp), %eax
	subl	$1, %eax
	imull	-28(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L122
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE34:
	.size	_Z22top_sec_diagonal_arrayIdEvPT_iiS0_, .-_Z22top_sec_diagonal_arrayIdEvPT_iiS0_
	.section	.text._Z26top_and_sec_diagonal_arrayIdEvPT_iiS0_,"axG",@progbits,_Z26top_and_sec_diagonal_arrayIdEvPT_iiS0_,comdat
	.weak	_Z26top_and_sec_diagonal_arrayIdEvPT_iiS0_
	.type	_Z26top_and_sec_diagonal_arrayIdEvPT_iiS0_, @function
_Z26top_and_sec_diagonal_arrayIdEvPT_iiS0_:
.LFB35:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movsd	%xmm0, -40(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L124
.L127:
	movl	$0, -8(%rbp)
	jmp	.L125
.L126:
	movl	-4(%rbp), %edx
	movl	-8(%rbp), %eax
	addl	%edx, %eax
	cltq
	leaq	0(,%rax,8), %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movsd	-40(%rbp), %xmm0
	movsd	%xmm0, (%rax)
	addl	$1, -8(%rbp)
.L125:
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	movl	%eax, %edx
	movl	-32(%rbp), %eax
	subl	%edx, %eax
	cmpl	%eax, -8(%rbp)
	jl	.L126
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L124:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L127
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE35:
	.size	_Z26top_and_sec_diagonal_arrayIdEvPT_iiS0_, .-_Z26top_and_sec_diagonal_arrayIdEvPT_iiS0_
	.section	.text._Z25bottom_sec_diagonal_arrayIdEvPT_iiS0_,"axG",@progbits,_Z25bottom_sec_diagonal_arrayIdEvPT_iiS0_,comdat
	.weak	_Z25bottom_sec_diagonal_arrayIdEvPT_iiS0_
	.type	_Z25bottom_sec_diagonal_arrayIdEvPT_iiS0_, @function
_Z25bottom_sec_diagonal_arrayIdEvPT_iiS0_:
.LFB36:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movsd	%xmm0, -40(%rbp)
	movl	-32(%rbp), %eax
	movl	%eax, -4(%rbp)
	jmp	.L129
.L132:
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	movl	%eax, %edx
	movl	-32(%rbp), %eax
	subl	%edx, %eax
	movl	%eax, -8(%rbp)
	jmp	.L130
.L131:
	movl	-4(%rbp), %edx
	movl	-8(%rbp), %eax
	addl	%edx, %eax
	cltq
	leaq	0(,%rax,8), %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movsd	-40(%rbp), %xmm0
	movsd	%xmm0, (%rax)
	addl	$1, -8(%rbp)
.L130:
	movl	-8(%rbp), %eax
	cmpl	-32(%rbp), %eax
	jl	.L131
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L129:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L132
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE36:
	.size	_Z25bottom_sec_diagonal_arrayIdEvPT_iiS0_, .-_Z25bottom_sec_diagonal_arrayIdEvPT_iiS0_
	.section	.text._Z29bottom_and_sec_diagonal_arrayIdEvPT_iiS0_,"axG",@progbits,_Z29bottom_and_sec_diagonal_arrayIdEvPT_iiS0_,comdat
	.weak	_Z29bottom_and_sec_diagonal_arrayIdEvPT_iiS0_
	.type	_Z29bottom_and_sec_diagonal_arrayIdEvPT_iiS0_, @function
_Z29bottom_and_sec_diagonal_arrayIdEvPT_iiS0_:
.LFB37:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	%edx, -32(%rbp)
	movsd	%xmm0, -40(%rbp)
	movl	-32(%rbp), %eax
	movl	%eax, -4(%rbp)
	jmp	.L134
.L137:
	movl	-32(%rbp), %eax
	leal	-1(%rax), %ecx
	movl	-4(%rbp), %eax
	cltd
	idivl	-32(%rbp)
	movl	%eax, %edx
	movl	%ecx, %eax
	subl	%edx, %eax
	movl	%eax, -8(%rbp)
	jmp	.L135
.L136:
	movl	-4(%rbp), %edx
	movl	-8(%rbp), %eax
	addl	%edx, %eax
	cltq
	leaq	0(,%rax,8), %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movsd	-40(%rbp), %xmm0
	movsd	%xmm0, (%rax)
	addl	$1, -8(%rbp)
.L135:
	movl	-8(%rbp), %eax
	cmpl	-32(%rbp), %eax
	jl	.L136
	movl	-32(%rbp), %eax
	addl	%eax, -4(%rbp)
.L134:
	movl	-28(%rbp), %eax
	imull	-32(%rbp), %eax
	cmpl	%eax, -4(%rbp)
	jl	.L137
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE37:
	.size	_Z29bottom_and_sec_diagonal_arrayIdEvPT_iiS0_, .-_Z29bottom_and_sec_diagonal_arrayIdEvPT_iiS0_
	.ident	"GCC: (Debian 11.3.0-11) 11.3.0"
	.section	.note.GNU-stack,"",@progbits
