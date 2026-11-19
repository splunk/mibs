#
# PySNMP MIB module GWTT-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gwd/GWTT-SMI
# Produced by pysmi-1.1.12 at Thu Nov 19 08:35:21 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ModuleIdentity, iso, Unsigned32, NotificationType, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Integer32, Gauge32, MibIdentifier, Counter32, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "iso", "Unsigned32", "NotificationType", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Integer32", "Gauge32", "MibIdentifier", "Counter32", "TimeTicks", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
gwtt = MibIdentifier((1, 3, 6, 1, 4, 1, 10072))
chips = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 1))
devices = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 2))
cards = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 3))
snmpProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 4))
mibBuilder.exportSymbols("GWTT-SMI", cards=cards, devices=devices, chips=chips, gwtt=gwtt, snmpProxy=snmpProxy)
