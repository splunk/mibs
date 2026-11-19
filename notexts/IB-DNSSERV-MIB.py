#
# PySNMP MIB module IB-DNSSERV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/infoblox/IB-DNSSERV-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:36:27 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ibDNSServ, IbString = mibBuilder.importSymbols("IB-SMI-MIB", "ibDNSServ", "IbString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Counter64, ModuleIdentity, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso, MibIdentifier, Bits, ObjectIdentity, enterprises, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "ModuleIdentity", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso", "MibIdentifier", "Bits", "ObjectIdentity", "enterprises", "NotificationType", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibDnsServMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 32, 1))
ibDnsServMIBModule.setRevisions(('2011-07-13 00:00',))
if mibBuilder.loadTexts: ibDnsServMIBModule.setLastUpdated('201107130000Z')
if mibBuilder.loadTexts: ibDnsServMIBModule.setOrganization('Infoblox')
ibDnsServMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 32, 1, 1))
ibDnsServConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 32, 1, 1, 1))
ibDnsServConfigImplementIdent = MibScalar((1, 3, 6, 1, 4, 1, 32, 1, 1, 1, 1), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDnsServConfigImplementIdent.setStatus('current')
mibBuilder.exportSymbols("IB-DNSSERV-MIB", ibDnsServConfigImplementIdent=ibDnsServConfigImplementIdent, ibDnsServMIBObjects=ibDnsServMIBObjects, ibDnsServConfig=ibDnsServConfig, ibDnsServMIBModule=ibDnsServMIBModule, PYSNMP_MODULE_ID=ibDnsServMIBModule)
