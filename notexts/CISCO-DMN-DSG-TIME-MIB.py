#
# PySNMP MIB module CISCO-DMN-DSG-TIME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DMN-DSG-TIME-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGTime = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 23))
ciscoDSGTime.setRevisions(('2010-08-30 11:00', '2010-04-12 06:00', '2009-12-20 12:00',))
if mibBuilder.loadTexts: ciscoDSGTime.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoDSGTime.setOrganization('Cisco Systems, Inc.')
timeInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 23, 1))
timeFormat = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 23, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("twentyFourHr", 1), ("twentyFourHrSuspendZero", 2), ("twelveHr", 3), ("twelveHrSuspendZero", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeFormat.setStatus('current')
timeDateFormat = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 23, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("yyyymmdd", 1), ("ddmmyyyy", 2), ("mmddyyyy", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeDateFormat.setStatus('current')
timeGMTOffset = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 23, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33))).clone(namedValues=NamedValues(("minusTwelve", 1), ("minusEleven", 2), ("minusTen", 3), ("minusNine", 4), ("minusEight", 5), ("minusSeven", 6), ("minusSix", 7), ("minusFive", 8), ("minusFour", 9), ("minusThreeAndAHalf", 10), ("minusTwo", 12), ("minusOne", 13), ("zeroGMT", 14), ("plusOne", 15), ("plusTwo", 16), ("plusThree", 17), ("plusThreeAndAHalf", 18), ("plusFour", 19), ("plusFourAndAHalf", 20), ("plusFive", 21), ("plusFiveAndAHalf", 22), ("plusFiveAndThreeQuarter", 23), ("plusSix", 24), ("plusSixAndAHalf", 25), ("plusSeven", 26), ("plusEight", 27), ("plusNine", 28), ("plusNineAndAHalf", 29), ("plusTen", 30), ("plusEleven", 31), ("plusTwelve", 32), ("plusThirteen", 33)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeGMTOffset.setStatus('current')
timeCurrent = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 23, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeCurrent.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-TIME-MIB", PYSNMP_MODULE_ID=ciscoDSGTime, ciscoDSGTime=ciscoDSGTime, timeDateFormat=timeDateFormat, timeInfo=timeInfo, timeCurrent=timeCurrent, timeFormat=timeFormat, timeGMTOffset=timeGMTOffset)
