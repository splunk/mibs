#
# PySNMP MIB module CISCOSB-Redistribute (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-Redistribute
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ipSpec, = mibBuilder.importSymbols("CISCOSB-IP", "ipSpec")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
class RlRedistSrcProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("rlRedistProtocolConnected", 1), ("rlRedistProtocolStatic", 2), ("rlRedistProtocolRip", 3), ("rlRedistProtocolOspfv2", 4), ("rlRedistProtocolOspfv3", 5), ("rlRedistProtocolBgp", 6), ("rlRedistProtocolEigrp", 7), ("rlRedistProtocolIsIs", 8), ("rlRedistProtocolMobile", 9), ("rlRedistProtocolAll", 10))

class RlRedistDstProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("rlRedistProtocolRip", 3), ("rlRedistProtocolOspfv2", 4), ("rlRedistProtocolOspfv3", 5), ("rlRedistProtocolBgp", 6), ("rlRedistProtocolEigrp", 7), ("rlRedistProtocolIsIs", 8), ("rlRedistProtocolMobile", 9))

class RlRedistMatchType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("rlRedistMatchTypeNone", 0), ("rlRedistMatchTypeInternal", 1), ("rlRedistMatchTypeExternalOne", 2), ("rlRedistMatchTypeExternalTwo", 3))

class RlRedistMetricType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("rlRedistMetricTypeNone", 0), ("rlRedistMetricTypeExternalOne", 1), ("rlRedistMetricTypeExternalTwo", 2))

rlRedistribute = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27))
rlRedistTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1), )
if mibBuilder.loadTexts: rlRedistTable.setStatus('current')
rlRedistEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1), ).setIndexNames((0, "CISCOSB-Redistribute", "rlRedistDstProtocol"), (0, "CISCOSB-Redistribute", "rlRedistSrcProtocol"), (0, "CISCOSB-Redistribute", "rlRedistDstProcessId"), (0, "CISCOSB-Redistribute", "rlRedistSrcProcessId"), (0, "CISCOSB-Redistribute", "rlRedistMatchType"), (0, "CISCOSB-Redistribute", "rlRedistRoutMapName"))
if mibBuilder.loadTexts: rlRedistEntry.setStatus('current')
rlRedistDstProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 1), RlRedistDstProtocol())
if mibBuilder.loadTexts: rlRedistDstProtocol.setStatus('current')
rlRedistSrcProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 2), RlRedistSrcProtocol())
if mibBuilder.loadTexts: rlRedistSrcProtocol.setStatus('current')
rlRedistDstProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: rlRedistDstProcessId.setStatus('current')
rlRedistSrcProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: rlRedistSrcProcessId.setStatus('current')
rlRedistMatchType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 5), RlRedistMatchType())
if mibBuilder.loadTexts: rlRedistMatchType.setStatus('current')
rlRedistRoutMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: rlRedistRoutMapName.setStatus('current')
rlRedistAsNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRedistAsNumber.setStatus('current')
rlRedistMetricTransparent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 8), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRedistMetricTransparent.setStatus('current')
rlRedistMetricValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRedistMetricValue.setStatus('current')
rlRedistMetricType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 10), RlRedistMetricType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRedistMetricType.setStatus('current')
rlRedistSubnets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 11), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRedistSubnets.setStatus('current')
rlRedistOnlyNSSA = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 12), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRedistOnlyNSSA.setStatus('current')
rlRedistRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlRedistRowStatus.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-Redistribute", RlRedistMatchType=RlRedistMatchType, rlRedistMetricTransparent=rlRedistMetricTransparent, rlRedistTable=rlRedistTable, rlRedistSubnets=rlRedistSubnets, rlRedistSrcProtocol=rlRedistSrcProtocol, rlRedistEntry=rlRedistEntry, rlRedistAsNumber=rlRedistAsNumber, rlRedistribute=rlRedistribute, rlRedistRoutMapName=rlRedistRoutMapName, rlRedistRowStatus=rlRedistRowStatus, RlRedistDstProtocol=RlRedistDstProtocol, rlRedistOnlyNSSA=rlRedistOnlyNSSA, rlRedistMatchType=rlRedistMatchType, rlRedistDstProtocol=rlRedistDstProtocol, rlRedistSrcProcessId=rlRedistSrcProcessId, rlRedistMetricType=rlRedistMetricType, RlRedistSrcProtocol=RlRedistSrcProtocol, RlRedistMetricType=RlRedistMetricType, rlRedistMetricValue=rlRedistMetricValue, rlRedistDstProcessId=rlRedistDstProcessId)
