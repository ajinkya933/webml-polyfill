model = Model()
i1 = Input("input", "TENSOR_QUANT8_ASYMM", "{2, 3}, 1.0, 0")
begins = Parameter("begins", "TENSOR_INT32", "{2}", [0, 0])
ends = Parameter("ends", "TENSOR_INT32", "{2}", [2, 3])
strides = Parameter("strides", "TENSOR_INT32", "{2}", [1, 1])
beginMask = Int32Scalar("beginMask", 0)
endMask = Int32Scalar("endMask", 0)
shrinkAxisMask = Int32Scalar("shrinkAxisMask", 1)

output = Output("output", "TENSOR_QUANT8_ASYMM", "{3}, 1.0, 0")

model = model.Operation("STRIDED_SLICE", i1, begins, ends, strides, beginMask, endMask, shrinkAxisMask).To(output)

# Example 1. Input in operand 0,
input0 = {i1: # input 0
          [1, 2, 3, 4, 5, 6]}

output0 = {output: # output 0
           [1, 2, 3]}

# Instantiate an example
Example((input0, output0))
