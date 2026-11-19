#
# PySNMP MIB module DLINK-ID-REC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINK-ID-REC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:48 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, Bits, ModuleIdentity, IpAddress, iso, enterprises, NotificationType, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "Bits", "ModuleIdentity", "IpAddress", "iso", "enterprises", "NotificationType", "MibIdentifier", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class AgentNotifyLevel(TextualConvention, Integer32):
    description = 'Notification  leveling.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("critical", 0), ("warning", 1), ("information", 2), ("emergency", 3), ("alert", 4), ("error", 5), ("notice", 6), ("debug", 7))

dlink = MibIdentifier((1, 3, 6, 1, 4, 1, 171))
dlink_products = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10)).setLabel("dlink-products")
dlink_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11)).setLabel("dlink-mgmt")
dlink_common_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12)).setLabel("dlink-common-mgmt")
dlinkIndustrialCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14))
dlink_broadband_products = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 30)).setLabel("dlink-broadband-products")
dlink_broadband_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 31)).setLabel("dlink-broadband-mgmt")
mibBuilder.exportSymbols("DLINK-ID-REC-MIB", AgentNotifyLevel=AgentNotifyLevel, dlinkIndustrialCommon=dlinkIndustrialCommon, dlink_broadband_products=dlink_broadband_products, dlink_broadband_mgmt=dlink_broadband_mgmt, dlink=dlink, dlink_common_mgmt=dlink_common_mgmt, dlink_mgmt=dlink_mgmt, dlink_products=dlink_products)
