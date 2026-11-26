#
# PySNMP MIB module LANOPTICS-ETHERNET-OPTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/LANOPTICS-ETHERNET-OPTION-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, enterprises, ModuleIdentity, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "enterprises", "ModuleIdentity", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lanOptics = MibIdentifier((1, 3, 6, 1, 4, 1, 224))
lanOpticsDot3Monitor = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 3))
etAlertsLevel = MibScalar((1, 3, 6, 1, 4, 1, 224, 3, 1), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etAlertsLevel.setStatus('mandatory')
etAlertsBuffer = MibScalar((1, 3, 6, 1, 4, 1, 224, 3, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etAlertsBuffer.setStatus('mandatory')
etFullStatisticsBuffer = MibScalar((1, 3, 6, 1, 4, 1, 224, 3, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etFullStatisticsBuffer.setStatus('mandatory')
etResetBuffers = MibScalar((1, 3, 6, 1, 4, 1, 224, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etResetBuffers.setStatus('mandatory')
etSlotsTable = MibTable((1, 3, 6, 1, 4, 1, 224, 3, 5), )
if mibBuilder.loadTexts: etSlotsTable.setStatus('mandatory')
pysmiFakeCol1004 = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 3, 5, 1) + (1004, ), Integer32())
etSlotsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 224, 3, 5, 1), ).setIndexNames((0, "LANOPTICS-ETHERNET-OPTION-MIB", "pysmiFakeCol1004"))
if mibBuilder.loadTexts: etSlotsEntry.setStatus('mandatory')
etSlotPollStruct = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 3, 5, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etSlotPollStruct.setStatus('mandatory')
mibBuilder.exportSymbols("LANOPTICS-ETHERNET-OPTION-MIB", etAlertsLevel=etAlertsLevel, etSlotsTable=etSlotsTable, etSlotsEntry=etSlotsEntry, lanOptics=lanOptics, pysmiFakeCol1004=pysmiFakeCol1004, etSlotPollStruct=etSlotPollStruct, etFullStatisticsBuffer=etFullStatisticsBuffer, etAlertsBuffer=etAlertsBuffer, lanOpticsDot3Monitor=lanOpticsDot3Monitor, etResetBuffers=etResetBuffers)
