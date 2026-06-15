`timescale 1ns/1ps
module testbench;
  reg clk = 0;
  reg reset = 1;
  reg [31:0] secret = 32'hDEADBEEF;
  reg [31:0] guess;
  wire match;
  wire [15:0] exec_cycles;
  vulnerable_comparator dut (.clk(clk), .reset(reset), .secret(secret), .guess(guess), .match(match), .execution_cycles(exec_cycles));
  always #5 clk = ~clk;
  initial begin
    $dumpfile("timing.vcd");
    $dumpvars(0, testbench);
    reset = 1; #10 reset = 0;
    #10 guess = 32'h00000000; #100;
    #20 guess = 32'hDEADBEEF; #100;
    #100 $finish;
  end
endmodule
