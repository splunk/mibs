#
# PySNMP MIB module DLINKSW-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-TC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:46 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, iso, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, ObjectIdentity, Unsigned32, MibIdentifier, Gauge32, Counter32, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Gauge32", "Counter32", "Counter64", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlinkSwTextualConvention = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 1))
dlinkSwTextualConvention.setRevisions(('2012-11-19 00:00',))
if mibBuilder.loadTexts: dlinkSwTextualConvention.setLastUpdated('201211190000Z')
if mibBuilder.loadTexts: dlinkSwTextualConvention.setOrganization('D-Link Corp.')
class DlinkTrigger(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("none", 1), ("action", 2))

class Dlink2kVlanList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

mibBuilder.exportSymbols("DLINKSW-TC-MIB", DlinkTrigger=DlinkTrigger, Dlink2kVlanList=Dlink2kVlanList, dlinkSwTextualConvention=dlinkSwTextualConvention, PYSNMP_MODULE_ID=dlinkSwTextualConvention)
