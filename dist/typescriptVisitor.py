# Generated from .\typescript.g4 by ANTLR 4.10
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .typescriptParser import typescriptParser
else:
    from typescriptParser import typescriptParser

# This class defines a complete generic visitor for a parse tree produced by typescriptParser.

class typescriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by typescriptParser#sAll.
    def visitSAll(self, ctx:typescriptParser.SAllContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sOperand.
    def visitSOperand(self, ctx:typescriptParser.SOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sOperator.
    def visitSOperator(self, ctx:typescriptParser.SOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sExpression.
    def visitSExpression(self, ctx:typescriptParser.SExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sTerm.
    def visitSTerm(self, ctx:typescriptParser.STermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sValue.
    def visitSValue(self, ctx:typescriptParser.SValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sInvocation.
    def visitSInvocation(self, ctx:typescriptParser.SInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sControl.
    def visitSControl(self, ctx:typescriptParser.SControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sStatement.
    def visitSStatement(self, ctx:typescriptParser.SStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sPlus.
    def visitSPlus(self, ctx:typescriptParser.SPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sMinus.
    def visitSMinus(self, ctx:typescriptParser.SMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sMul.
    def visitSMul(self, ctx:typescriptParser.SMulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sDiv.
    def visitSDiv(self, ctx:typescriptParser.SDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sPower.
    def visitSPower(self, ctx:typescriptParser.SPowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sAnd.
    def visitSAnd(self, ctx:typescriptParser.SAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sOr.
    def visitSOr(self, ctx:typescriptParser.SOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sNot.
    def visitSNot(self, ctx:typescriptParser.SNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sEquals.
    def visitSEquals(self, ctx:typescriptParser.SEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sNotEquals.
    def visitSNotEquals(self, ctx:typescriptParser.SNotEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sLowerThan.
    def visitSLowerThan(self, ctx:typescriptParser.SLowerThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sLowerEquals.
    def visitSLowerEquals(self, ctx:typescriptParser.SLowerEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sGreaterThan.
    def visitSGreaterThan(self, ctx:typescriptParser.SGreaterThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sGreaterEquals.
    def visitSGreaterEquals(self, ctx:typescriptParser.SGreaterEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sArithmeticExpression.
    def visitSArithmeticExpression(self, ctx:typescriptParser.SArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sArithmeticTerm.
    def visitSArithmeticTerm(self, ctx:typescriptParser.SArithmeticTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sBooleanOperand.
    def visitSBooleanOperand(self, ctx:typescriptParser.SBooleanOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sBooleanOperator.
    def visitSBooleanOperator(self, ctx:typescriptParser.SBooleanOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sBooleanExpression.
    def visitSBooleanExpression(self, ctx:typescriptParser.SBooleanExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sBooleanTerm.
    def visitSBooleanTerm(self, ctx:typescriptParser.SBooleanTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sNumberOperand.
    def visitSNumberOperand(self, ctx:typescriptParser.SNumberOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sNumberOperator.
    def visitSNumberOperator(self, ctx:typescriptParser.SNumberOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sNumberExpression.
    def visitSNumberExpression(self, ctx:typescriptParser.SNumberExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sNumberTerm.
    def visitSNumberTerm(self, ctx:typescriptParser.SNumberTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sStringOperand.
    def visitSStringOperand(self, ctx:typescriptParser.SStringOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sStringOperator.
    def visitSStringOperator(self, ctx:typescriptParser.SStringOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sStringExpression.
    def visitSStringExpression(self, ctx:typescriptParser.SStringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sStringTerm.
    def visitSStringTerm(self, ctx:typescriptParser.SStringTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sConcatOperand.
    def visitSConcatOperand(self, ctx:typescriptParser.SConcatOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sConcatExpression.
    def visitSConcatExpression(self, ctx:typescriptParser.SConcatExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sConcatLeft.
    def visitSConcatLeft(self, ctx:typescriptParser.SConcatLeftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sConcatRight.
    def visitSConcatRight(self, ctx:typescriptParser.SConcatRightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sConcatBoth.
    def visitSConcatBoth(self, ctx:typescriptParser.SConcatBothContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sType.
    def visitSType(self, ctx:typescriptParser.STypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sOptional.
    def visitSOptional(self, ctx:typescriptParser.SOptionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sPropertyDelete.
    def visitSPropertyDelete(self, ctx:typescriptParser.SPropertyDeleteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sFunction.
    def visitSFunction(self, ctx:typescriptParser.SFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sFunctionArg.
    def visitSFunctionArg(self, ctx:typescriptParser.SFunctionArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sFunctionArgs.
    def visitSFunctionArgs(self, ctx:typescriptParser.SFunctionArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sFunctionArgDef.
    def visitSFunctionArgDef(self, ctx:typescriptParser.SFunctionArgDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sFunctionArgDefs.
    def visitSFunctionArgDefs(self, ctx:typescriptParser.SFunctionArgDefsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sFunctionHead.
    def visitSFunctionHead(self, ctx:typescriptParser.SFunctionHeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sFunctionTail.
    def visitSFunctionTail(self, ctx:typescriptParser.SFunctionTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sFunctionCall.
    def visitSFunctionCall(self, ctx:typescriptParser.SFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sFunctionLambda.
    def visitSFunctionLambda(self, ctx:typescriptParser.SFunctionLambdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sProperty.
    def visitSProperty(self, ctx:typescriptParser.SPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sPropertyAware.
    def visitSPropertyAware(self, ctx:typescriptParser.SPropertyAwareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sPropertyAccess.
    def visitSPropertyAccess(self, ctx:typescriptParser.SPropertyAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sFunctionAware.
    def visitSFunctionAware(self, ctx:typescriptParser.SFunctionAwareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sFunctionAccess.
    def visitSFunctionAccess(self, ctx:typescriptParser.SFunctionAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sLine.
    def visitSLine(self, ctx:typescriptParser.SLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sBody.
    def visitSBody(self, ctx:typescriptParser.SBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sReturn.
    def visitSReturn(self, ctx:typescriptParser.SReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sIf.
    def visitSIf(self, ctx:typescriptParser.SIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sElse.
    def visitSElse(self, ctx:typescriptParser.SElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sElseIf.
    def visitSElseIf(self, ctx:typescriptParser.SElseIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sString.
    def visitSString(self, ctx:typescriptParser.SStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sNumber.
    def visitSNumber(self, ctx:typescriptParser.SNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sBoolean.
    def visitSBoolean(self, ctx:typescriptParser.SBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sArray.
    def visitSArray(self, ctx:typescriptParser.SArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sMap.
    def visitSMap(self, ctx:typescriptParser.SMapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sEndlessLoop.
    def visitSEndlessLoop(self, ctx:typescriptParser.SEndlessLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sWhile.
    def visitSWhile(self, ctx:typescriptParser.SWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sDoWhile.
    def visitSDoWhile(self, ctx:typescriptParser.SDoWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sFor.
    def visitSFor(self, ctx:typescriptParser.SForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sForOf.
    def visitSForOf(self, ctx:typescriptParser.SForOfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sForIn.
    def visitSForIn(self, ctx:typescriptParser.SForInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sLoopTail.
    def visitSLoopTail(self, ctx:typescriptParser.SLoopTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sContinue.
    def visitSContinue(self, ctx:typescriptParser.SContinueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sBreak.
    def visitSBreak(self, ctx:typescriptParser.SBreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sMutableVar.
    def visitSMutableVar(self, ctx:typescriptParser.SMutableVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sImmutableVar.
    def visitSImmutableVar(self, ctx:typescriptParser.SImmutableVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sAssignment.
    def visitSAssignment(self, ctx:typescriptParser.SAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sIncrement.
    def visitSIncrement(self, ctx:typescriptParser.SIncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by typescriptParser#sDecrement.
    def visitSDecrement(self, ctx:typescriptParser.SDecrementContext):
        return self.visitChildren(ctx)



del typescriptParser