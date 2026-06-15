`timescale 1ns/1ps
module vulnerable_comparator(input clk, input reset, input [31:0] secret, input [31:0] guess, output reg match, output reg [15:0] execution_cycles);
always @(posedge clk) begin
  if (reset) begin match = 1'b0; execution_cycles = 16'd0; end
  else begin match = 1'b1; execution_cycles = 16'd0;
    for (integer i = 31; i >= 0; i = i - 1) begin
      execution_cycles = execution_cycles + 10;
      if (secret[i] != guess[i]) match = 1'b0;
    end
  end
end
endmodule
