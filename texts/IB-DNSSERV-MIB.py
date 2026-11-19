#
# PySNMP MIB module IB-DNSSERV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/infoblox/IB-DNSSERV-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:36:27 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
IbString, ibDNSServ = mibBuilder.importSymbols("IB-SMI-MIB", "IbString", "ibDNSServ")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, Gauge32, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, enterprises, Bits, Integer32, iso, ModuleIdentity, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Gauge32", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "enterprises", "Bits", "Integer32", "iso", "ModuleIdentity", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibDnsServMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 32, 1))
ibDnsServMIBModule.setRevisions(('2011-07-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ibDnsServMIBModule.setRevisionsDescriptions(('Creation of the DNS Server MIB file',))
if mibBuilder.loadTexts: ibDnsServMIBModule.setLastUpdated('201107130000Z')
if mibBuilder.loadTexts: ibDnsServMIBModule.setOrganization('Infoblox')
if mibBuilder.loadTexts: ibDnsServMIBModule.setContactInfo('Please See IB-SMI-MIB.')
if mibBuilder.loadTexts: ibDnsServMIBModule.setDescription('This file defines the Infoblox DNS Server MIB.')
ibDnsServMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 32, 1, 1))
ibDnsServConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 32, 1, 1, 1))
ibDnsServConfigImplementIdent = MibScalar((1, 3, 6, 1, 4, 1, 32, 1, 1, 1, 1), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDnsServConfigImplementIdent.setStatus('current')
if mibBuilder.loadTexts: ibDnsServConfigImplementIdent.setDescription('The implementation identification string for\n                  the DNS server software in use on the system.')
mibBuilder.exportSymbols("IB-DNSSERV-MIB", ibDnsServMIBModule=ibDnsServMIBModule, ibDnsServConfig=ibDnsServConfig, ibDnsServMIBObjects=ibDnsServMIBObjects, ibDnsServConfigImplementIdent=ibDnsServConfigImplementIdent, PYSNMP_MODULE_ID=ibDnsServMIBModule)
